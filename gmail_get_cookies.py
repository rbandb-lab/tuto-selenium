# user: yannick.test.selenium
# password: test_selenium.123
# pip install undetected-chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pickle

# import undetected_chromedriver as uc
# TBD:// use undetected_chromedriver and 2FA to test if selenium is really undetected

try:
    test_email = 'yannick.test.selenium'
    test_passwd = 'test_selenium.123'
    browser = webdriver.Chrome()
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    # input username
    browser.find_element(By.ID, 'identifierId').send_keys(test_email)
    browser.find_element(By.CSS_SELECTOR, '#identifierNext > div > button').click()

    # wait for password form field to be visible and send password
    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))
    browser.find_element(By.CSS_SELECTOR, password_selector).send_keys(test_passwd)

    # validate password
    browser.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
except Exception as e:
    print(e, "error ")
pass

# TBD:// wait for selector
time.sleep(5)
cookies = browser.get_cookies()
pickle.dump(cookies, open("cookies.pkl", "wb"))
