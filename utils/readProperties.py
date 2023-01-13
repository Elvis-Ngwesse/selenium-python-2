import configparser
from configurations.filePath import get_configini_file_path
from utils.rapper_function import func_loger

config = configparser.RawConfigParser()
config_path = get_configini_file_path()
config.read(config_path)


class ReadConfig:

    @staticmethod
    @func_loger
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    @func_loger
    def get_browser_type():
        browser_type = config.get('common info', 'browser_type')
        return browser_type

    @staticmethod
    @func_loger
    def get_headless():
        headless = config.get('common info', 'headless_browser')
        if headless == 'True':
            return True
        else:
            return False
