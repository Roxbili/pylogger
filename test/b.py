from logger import Logger

log_path = 'test_b.log'
logger = Logger(__name__, log_path).get_logger()

logger.info('this is b')
logger.info('b hello')