# define webpage elements here
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    locator = 'q'
    timeout = 100

    def __set__(self, obj, value):
        '''setter dunder method'''
        driver = obj.driver
        WebDriverWait(driver, self.timeout).until(
                lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        '''getter dunder method'''
        driver = obj.driver
        WebDriverWait(driver, self.timeout).until(
                lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute('value')

class SearchTextElement(BasePageElement):
    '''
    <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
    '''
    # this overrides the locator in BasePageElement
    locator = 'q'