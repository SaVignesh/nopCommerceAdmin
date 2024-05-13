import inspect
import logging

class LogGen:
    @staticmethod
    def loggen():

        logger_name = inspect.stack()[1][3]    # To get class name to be displayed in the logs
        logger = logging.getLogger(logger_name)
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
