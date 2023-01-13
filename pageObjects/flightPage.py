from selenium.webdriver.common.by import By
from src.baseClass import BaseClass


class FlightPage:
    __book_flight_locator = "li[class='book_flight']"

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__book_flight_locator)
