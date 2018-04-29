from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def test_login():
    """ Test login functionality """
    driver.get('http://127.0.0.1:8000/login')
    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    submit = driver.find_element_by_class_name('btn')

    username.send_keys('doctor_kumar')
    password.send_keys('pass@admin')

    submit.send_keys(Keys.RETURN)
    return('Log Out' in driver.page_source)

driver = webdriver.Chrome()

def test_logout():
    """ Test logout functionality """
    log_out = driver.find_element_by_id('logout')
    log_out.send_keys(Keys.RETURN)
    return('Login' in driver.page_source)

if test_login():
    print('Login test OK')
    if test_logout():
        print('Logout test OK')
    else:
        print('Logout test failed')
else:
    print('Login test failed')

driver.quit()
