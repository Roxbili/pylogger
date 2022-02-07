from logger import Logger

def msg():
    log_path = 'test_b.log'
    logger = Logger(__name__).get_logger()

    logger.info('this is b')
    logger.info('b hello')