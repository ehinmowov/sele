from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


"""a

Please refer to the GIUs.py doc to see exactly how i sent the inputs to the crawler

I have defined a special function for each action so that it would be easy for you

"""


def fill_supwork_form():
    options = Options()
    options.add_argument("user-agent=[user-agent string]")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    global driver
    # driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
    driver = webdriver.Chrome('/Users/director/Desktop/databoy/chromedriver', chrome_options=options)
    driver.get('http://www.sup.work/tr')


def access_form():
    client_signup_button = driver.find_element_by_id('clientSignUp')
    csbs = client_signup_button.screenshot_as_png
    client_signup_button.click()
    sleep(2)


'''This is one of the inputs the crawler receives from the GIUs doc'''
def input_firstname(fn):
    first_name = driver.find_element_by_id('firstName')
    first_name.send_keys(fn)


def input_lastname(ln):
    last_name = driver.find_element_by_id('lastName')
    last_name.send_keys(ln)
    sleep(2)


def input_email():
    email = driver.find_element_by_id('email')
    email.send_keys('bigboy@gmail.com')
    sleep(2)


def select_nationality():
    nationality = driver.find_element_by_id('nationality')
    drop_nationality = Select(nationality)
    drop_nationality.select_by_value('Nigeria')


def input_address():
    address = driver.find_element_by_id('address')
    address.send_keys('Atilkan block 10, room 5')


def select_apt_size():
    apt_size = driver.find_element_by_id('houseType')
    drop_apt_size = Select(apt_size)
    drop_apt_size.select_by_value('3+1')
    sleep(2)


def select_lang():
    lang = driver.find_element_by_id('language')
    drop_lang = Select(lang)
    drop_lang.select_by_value('en')


def select_prop():
    prop = driver.find_element_by_id('property')
    drop_property = Select(prop)
    drop_property.select_by_value('Home')


def input_number():
    number = driver.find_element_by_id('phone')
    number.send_keys('+905488241162')
    sleep(2)


def close_form():
    close_button = driver.find_element_by_class_name('close')
    close_button.click()
    sleep(2)

    driver.close()
