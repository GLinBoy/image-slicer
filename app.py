import logging, os
import cv2


logging.basicConfig(format='%(levelname)s | %(asctime)s | %(message)s', level=logging.INFO)


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


def main():
    images = get_files('./images')
    for img in images:
        logging.info(img)


if __name__ == '__main__':
    main()
