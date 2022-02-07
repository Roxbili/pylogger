from logger import Logger

log_path = 'test.log'
logger = Logger(log_path, __name__).get_logger()

logger.info('this is b')
logger.info('b hello')