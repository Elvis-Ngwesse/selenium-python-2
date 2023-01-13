import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from configurations.context import Context
from utils.customLogger import LogGeneration
import os
log = LogGeneration.loggen()


class BaseClass:

    @staticmethod
    def thread_sleep(time_in_seconds: int):
        """
        Make a function sleep
        """
        time.sleep(time_in_seconds)

    @staticmethod
    def take_screenshot(name: str):
        """
        This function takes a screenshot
        :param name: name of the screenshot
        """
        working_dir = os.getcwd()
        screenshots_dir = working_dir.replace('testCases', 'screenshots/')
        try:
            Context.driver.save_screenshot(f'{screenshots_dir}' + f'{name}.png')
            log.info('Screen shot successfully taken')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def find_elements(by, web_element):
        """
        This function finds a list of webelements
        :param by: method to locate web-element
        :param web_element: locator
        :return: returns a list of webelements
        """
        try:
            elements = Context.driver.find_elements(by, web_element)
            log.info(f'Web-elements successfully returned: {web_element}')
            return elements
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def switch_to_new_window_and_back(window_before: int, window_after: int):
        """
        Switch to new window,close window, and navigate back to original window
        :param window_before:
        :param window_after:
        """
        try:
            _window_before = Context.driver.window_handles[window_before]
            _window_after = Context.driver.window_handles[window_after]
            Context.driver.switch_to.window(_window_after)
            url = BaseClass.page_url()
            Context.driver.close()
            log.info(f'Successfully switched and closed new window')
            Context.driver.switch_to.window(_window_before)
            log.info(f'Successfully switched back to original window')
            return url
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def switch_to_new_window(window_after: int):
        """
        Switch to new windo
        :param window_after:
        """
        try:
            _window_after = Context.driver.window_handles[window_after]
            Context.driver.switch_to.window(_window_after)
            log.info(f'Successfully switched to new window')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def find_element(by, web_element):
        """
        This function finds a web-element
        :param by: method to locate web-element
        :param web_element: locator
        :return: returns a web-element
        """
        try:
            element = Context.driver.find_element(by, web_element)
            log.info(f'Web-element successfully returned: {web_element}')
            return element
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def element_hover_over(by, web_element):
        """
        This function hovers over a web-element
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element_to_hover = Context.driver.find_element(by, web_element)
            hover = ActionChains(Context.driver).move_to_element(element_to_hover)
            hover.perform()
            log.info(f'Web-element hover-over successful: {web_element}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def switch_to_iframe(by, web_element):
        """
        This function switches to a frame on a web page
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            iframe = Context.driver.find_element(by, web_element)
            Context.driver.switch_to.frame(iframe)
            log.info(f'Successfully switched to iframe: {iframe}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def switch_to_default_content():
        """
        This function switches back to default content
        """
        try:
            Context.driver.switch_to.default_content()
            log.info(f'Successfully switched to default content')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def accept_alert():
        """
        This function accepts an alert
        """
        try:
            alert = Context.driver.switch_to.alert
            alert.accept()
            log.info(f'Successfully accepted alert')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def dismiss_alert():
        """
        This function dismisses an alert
        """
        try:
            alert = Context.driver.switch_to.alert
            alert.dismiss()
            log.info(f'Successfully dismissed alert')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def page_url():
        """
        This function gets page url
        """
        try:
            url = Context.driver.current_url
            log.info(f'Successfully returned url')
            return url
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def double_click(by, web_element):
        """
        This function double click on web-element
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element = Context.driver.find_element(by, web_element)
            action = ActionChains(Context.driver)
            action.double_click(on_element=element)
            action.perform()
            log.info(f'Successfully double clicked on web-element')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def attribute_value(by, web_element, attribute: str):
        """
        This function gets web-element attribute value
        :param attribute: element attribute
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element = Context.driver.find_element(by, web_element)
            results = element.get_attribute(attribute)
            log.info(f'Successfully returned attribute value')
            return results
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def page_tittle():
        """
        This function gets page url
        """
        try:
            url = Context.driver.title
            log.info(f'Successfully returned page title')
            return url
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def element_click(by, web_element):
        """
        This function clicks on a web-element
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element_to_click = Context.driver.find_element(by, web_element)
            element_to_click.click()
            log.info(f'Successfully clicked on web-element: {web_element}')
        except Exception as error:
            if NoSuchElementException in error:
                element_to_hover = Context.driver.find_element(by, web_element)
                hover = ActionChains(Context.driver).move_to_element(element_to_hover)
                hover.perform()

                element_to_click = Context.driver.find_element(by, web_element)
                element_to_click.click()
                log.info(f'Successfully clicked on web-element: {web_element}')
            else:
                log.error(error)
                raise error

    @staticmethod
    def element_wait(by, web_element):
        """
        This function waits for a web-element to be present in the dome
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            WebDriverWait(Context.driver, 10).until(wait.presence_of_element_located((by, web_element)))
            log.info(f'Successfully waited for web-element: {web_element}')
        except TimeoutException as error:
            log.error(error.msg)
            raise error

    @staticmethod
    def clear_text(by, web_element):
        """
        This function clears text in a field
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element_to_clear = Context.driver.find_element(by, web_element)
            element_to_clear.clear()
            log.info(f'Successfully cleared text on web-element: {web_element}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def set_text(by, web_element, text):
        """
        This function sets enters to a field
        :param by: method to locate web-element
        :param web_element: locator
        :param text: text to enter
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element_to_set = Context.driver.find_element(by, web_element)
            element_to_set.send_keys(text)
            log.info(f'Successfully set text on web-element: {web_element}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def element_is_visible(by, web_element):
        """
        This function waits for element to be visible
        :param by: method to locate web-element
        :param web_element: locator
        :return: boolean value if element is visible or not
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element = Context.driver.find_element(by, web_element)
            presence_of_value = element.is_displayed()
            log.info(f'Successfully checked web-element visibility: {web_element}')
            return presence_of_value
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def is_page_loaded(by, web_element):
        """
        This function waits for page to be loaded
        :param by: method to locate web-element
        :param web_element: locator
        :return: boolean value if page is loaded or not
        """
        try:
            element = Context.driver.find_element(by, web_element)
            WebDriverWait(Context.driver, 15).until(wait.presence_of_element_located((by, web_element)))
            presence_of_value = element.is_displayed()
            log.info(f'Page load successfully')
            return presence_of_value
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def is_element_clickable(by, web_element):
        """
        This function waits for element to be clickable
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            WebDriverWait(Context.driver, 10).until(wait.element_to_be_clickable((by, web_element)))
            log.info(f'Successfully checked web-element clickable: {web_element}')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def select_from_drop_down_by_text(by, web_element, text: str):
        """
        This function selects from dropdown
        :param text:
        :param by: method to locate web-element
        :param web_element: locator
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element = Context.driver.find_element(by, web_element)
            element.click()
            display_dropdown = Select(element)
            display_dropdown.select_by_visible_text(text=text)
            log.info(f'Successfully selected element from drop-down')
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def get_element_text(by, web_element):
        """
        This function gets the text embedded in a web-element
        :param by: method to locate web-element
        :param web_element: locator
        :return: returns text
        """
        try:
            BaseClass.element_wait(by=by, web_element=web_element)
            element = Context.driver.find_element(by, web_element)
            text = element.text
            log.info(f'Successfully returned web-element text: {web_element}')
            return text
        except Exception as error:
            log.error(error)
            raise error

    @staticmethod
    def navigate_to_link(url):
        """
        This function helps navigate to a new url
        :param url: Url to navigate to
        """
        try:
            Context.driver.get(url)
            log.info(f'Successfully navigated to URL: {url}')
        except Exception as error:
            log.error(error)
            raise error
