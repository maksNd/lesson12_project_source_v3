import logging


def get_and_set_logger():
    logger = logging.getLogger('basic')
    logger.setLevel(logging.DEBUG)

    formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter_one)

    logger.addHandler(console_handler)
