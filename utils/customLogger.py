import logging
import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

class LogGeneration:

    @staticmethod
    def loggen():
        """
        Configures the logger instance
        :return: Returns the logger instance
        """
        log = os.getcwd()
        log_dir = os.path.join(ROOT_DIR, f"logs/automation.log")
        logging.basicConfig(filename=log_dir,
                            level=logging.INFO,
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        return logger
