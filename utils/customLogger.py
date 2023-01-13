import logging
import os


class LogGeneration:

    @staticmethod
    def loggen():
        """
        Configures the logger instance
        :return: Returns the logger instance
        """
        log = os.getcwd()
        log_dir = log.replace('testCases', 'logs')
        logging.basicConfig(filename=log_dir+"/automation.log",
                            level=logging.INFO,
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        return logger
