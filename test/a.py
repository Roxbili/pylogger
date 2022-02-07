from logger import Logger
log_path = 'test.log'
logger = Logger(__name__, log_path=log_path).get_logger()

import b

logger.info('this is a')
logger.info('a hello')