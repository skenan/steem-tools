import logging
import os

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file_name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    fh = logging.FileHandler(os.path.join(os.path.dirname(__file__), os.pardir, 'logs', log_file_name), 'a',
                             'utf-8')
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
