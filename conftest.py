import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pageObjects.greenKartPage import GreenKartPage
from utils.readProperties import ReadConfig
import pytest
from configurations.context import Context
from selenium.webdriver.chrome.options import Options
from src.baseClass import BaseClass
from allure_commons.types import AttachmentType
from pytest_harvest import saved_fixture
import os
import glob
from threading import Lock
from utils.customLogger import LogGeneration

log = LogGeneration.loggen()


@pytest.fixture(autouse=True)
@saved_fixture  # to save all instances created. access using fixture_store
def setup(request):
    """
    Initialises test run
    :param request: Gets test context
    """
    try:

        options = Options()
        bool_object = ReadConfig.get_headless()
        options.headless = bool_object
        browser = ReadConfig.get_browser_type()
        log.info(f'Opening {browser} browser')
        if browser == 'chrome':
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        driver.set_window_size(1024, 600)
        driver.maximize_window()
        Context.driver = driver
        url = ReadConfig.get_application_url()
        Context.driver.get(url)
        test_name = request.node.name  # Get current test name
        _dir = os.getcwd()
        log_dir = _dir.replace('testCases', 'screenshots/*')

        # Delete files from screenshot folder
        files = glob.glob(log_dir)
        for f in files:
            os.remove(f)

        yield

        # Lock current thread execution
        lock = Lock()
        lock.acquire()

        # If test status is testsfailed? Take a screenshot
        test_exit_status = request.node.session.testsfailed
        if test_exit_status == 1:
            BaseClass.take_screenshot(test_name)
            allure.attach(driver.get_screenshot_as_png(), name=test_name, attachment_type=AttachmentType.PNG)
        lock.release()
        driver.quit()
        log.info(f'Closing {browser} browser')
    except Exception as error:
        log.error(error)
        raise error


@pytest.fixture()
def navigate_to_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page


@pytest.fixture()
def navigate_to_offers():
    green_kart_page = Context.green_kart_page
    green_kart_page.navigate_to_offers_page()


@pytest.fixture()
def top_deals():
    green_kart_page = Context.green_kart_page
    green_kart_page.click_on_top_deals()
