import b
from logger import Logger

log_path = 'test.log'
logger = Logger(__name__, log_path=log_path).get_logger()

logger.info('this is a')
logger.info('a hello')

b.msg()
b.msg()