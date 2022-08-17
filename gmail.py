# user: yannick.test.selenium
# password: test_selenium.123
# pip install undetected-chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# import undetected_chromedriver as uc


try:
    test_email = 'yannick.test.selenium'
    test_passwd = 'test_selenium.123'
    browser = webdriver.Chrome()
    browser.get('https://gmail.com')
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


