import pickle
import time

from selenium import webdriver
from os.path import exists
import undetected_chromedriver as uc

if not exists("cookies.pkl"):
    import gmail_get_cookies

# Load cookies to browser (those of same origin)
browser = uc.Chrome()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ".google.com"
    try:
        browser.add_cookie(cookie)
    except:
        print()

# visit inbox page ...
browser.get('https://mail.google.com/mail/u/0/#inbox')

time.sleep(120)