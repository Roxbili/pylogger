import logging

class Logger(object):
    '''Logger for file and terminal'''

    def __init__(self, log_path, logger_name, level='INFO',
                format='[%(levelname)s] [%(asctime)s] %(filename)s:%(lineno)d - %(message)s',
                datefmt='%m/%d %H:%M:%S'):
        '''Logger init

            Args:
                log_path: the path to save the log
                logger_name: name for new logger
                level: DEBUG, INFO, WARN, ERROR, CRITICAL, default: INFO
                format: logging format
        '''

        # logger basic config
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(self._get_level(level))

        # handler settings
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self._get_level(level))
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(self._get_level(level))

        # format settings
        formatter = logging.Formatter(format, datefmt=datefmt)
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def _get_level(self, level: str):
        log_level = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return log_level[level.upper()]

    def get_logger(self) -> logging:
        return self.logger