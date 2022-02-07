from logger import Logger
import b

log_path = 'test.log'
logger = Logger(log_path, __name__).get_logger()

logger.info('this is a')
logger.info('a hello')