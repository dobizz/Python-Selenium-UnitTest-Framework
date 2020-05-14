import unittest
import page
from selenium import webdriver as wd


class Webpage(unittest.TestCase):
    '''Example webpage test case class using Chromedriver'''
    
    def setUp(self):
        '''initialize webdriver'''
        '''this method will be called every time test cases are run'''
        print('Running setup')
        url = 'https://www.python.org'
        # location of chromedriver executable
        driver_path = '../drivers/chromedriver.exe'

        chrome_options = wd.ChromeOptions()
        # add optional webdriver arguments here
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--incognito')

        self.driver = wd.Chrome(driver_path, options=chrome_options)
        self.driver.get(url)


    def test_example(self):
        '''execute this sample test'''
        print('Running sample test')
        # create assert condition to be tested
        assert True


    def test_title(self):
        '''test page title'''
        print('Running title test')
        title = 'Python'
        home = page.HomePage(self.driver)
        assert home.is_title(title)


    def test_search(self):
        '''test search functionality'''
        print('Running search test')
        home = page.HomePage(self.driver)
        home.search_text_element = 'pycon'
        home.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()


    def tearDown(self):
        '''cleanup and close webdriver'''
        '''this method will be called every time after test cases are run'''
        print('Running cleanup')
        self.driver.close()


if __name__ == '__main__':
    unittest.main()