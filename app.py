import logging, os


logging.basicConfig(format='%(levelname)s | %(asctime)s | %(message)s', level=logging.INFO)


def get_files(path):
    logging.info('Reading File from: %s', path)
    images = []
    for file in os.listdir(path):
        if (file.endswith('.png') or file.endswith('.jpg')):
            images.append('{}/{}'.format(path, file))
    return images


def main():
    logging.info('Hello Python!')


if __name__ == '__main__':
    main()
