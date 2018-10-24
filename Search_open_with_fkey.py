from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pynput.keyboard import Key, Controller


class Search:
    def open_search_fkey(self):
        baseurl = 'https://candidx.io/'
        driver = webdriver.Chrome()
        # options.add_argument('--disable-extensions')
        # options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        driver.get(baseurl)
        driver.implicitly_wait(5)

        username_input = driver.find_element_by_name('userEmail')
        username_input.send_keys('amratest')

        password_input = driver.find_element_by_name('userPassword')
        password_input.send_keys('iQwuVCtqHQ1juU3')

        login_click = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/div/div')
        login_click.click()
        time.sleep(2)

        keyboard = Controller()
        keyboard.press('f')
        keyboard.release('f')
        time.sleep(1)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

searching = Search()
searching.open_search_fkey()
