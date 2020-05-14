# define page actions here

from locator import HomePageLocators
from element import BasePageElement, SearchTextElement


class BasePage(object):
    '''Base webpage class'''

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    '''Home page class'''

    search_text_element = SearchTextElement()

    def is_title(self, title):
        '''check if page title is equal to'''
        return title in self.driver.title

    def click_go_button(self):
        '''perform click of go button'''
        element = self.driver.find_element(*HomePageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    '''Search results class'''
    def is_results_found(self):
        return "No results found" not in self.driver.page_source

