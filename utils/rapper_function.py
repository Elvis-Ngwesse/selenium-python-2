from utils import customLogger

logger = customLogger.LogGeneration.loggen()


def func_loger(func):
    def wrap(*args, **kwargs):
        try:
            logger.info(f'{func.__name__}  execution started')
            result = func(*args, **kwargs)
            logger.info(f'{func.__name__}  execution successful')
            return result
        except Exception as error:
            logger.error(error)
            raise error

    return wrap
