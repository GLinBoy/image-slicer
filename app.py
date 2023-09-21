import logging
import os
import cv2
from fpdf import FPDF


logging.basicConfig(
    format='%(levelname)s | %(asctime)s | %(message)s', level=logging.INFO)


def split(filepath):
    directory, file_fullname = os.path.split(filepath)
    file_name, file_extension = os.path.splitext(file_fullname)

    img = cv2.imread(filepath)
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # Cut the image in half
    width_cutoff = width // 2
    s1 = img[:, :width_cutoff]
    s2 = img[:, width_cutoff:]

    cv2.imwrite('{}/splitted/{}_left{}'.format(directory,
                file_name, file_extension), s1)
    cv2.imwrite('{}/splitted/{}_right{}'.format(directory,
                file_name, file_extension), s2)


def get_files(path):
    logging.info('Reading File from: %s', path)
    images = []
    for file in os.listdir(path):
        if (file.endswith('.png') or file.endswith('.jpg')):
            images.append('{}/{}'.format(path, file))
    return images


def create_pdf(path, images_path):
    logging.info("Start to convert images to PDF")
    pdf = FPDF()
    # imagelist is the list with all image filenames
    for image in images_path:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
    pdf.output("{}/output.pdf".format(path), "F")


def main():
    images = get_files('./images')
    for img in images:
        split(img)


if __name__ == '__main__':
    main()
