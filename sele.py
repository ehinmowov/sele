from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


"""a

just trying to see

"""


def fill_supwork_form():
    global driver
    driver = webdriver.Chrome('/Users/director/Desktop/databoy/chromedriver')
    driver.get('http://www.sup.work/tr')


def access_form():
    client_signup_button = driver.find_element_by_id('clientSignUp')
    csbs = client_signup_button.screenshot_as_png
    client_signup_button.click()
    sleep(2)


def input_firstname(fn):
    first_name = driver.find_element_by_id('firstName')
    first_name.send_keys(fn)


def input_lastname(ln):
    last_name = driver.find_element_by_id('lastName')
    last_name.send_keys(ln)


def input_email():
    email = driver.find_element_by_id('email')
    email.send_keys('bigboy@gmail.com')


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
