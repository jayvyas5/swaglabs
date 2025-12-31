import inspect
import logging
import os
from config.config import TestData


class LoggerUtil:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        os.makedirs(os.path.dirname(TestData.LOG_FILE_PATH), exist_ok=True)

        filehandler = logging.FileHandler(TestData.LOG_FILE_PATH)
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :%(name)s :%(message)s"
        )
        filehandler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger
