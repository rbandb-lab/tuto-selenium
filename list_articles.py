from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    print("All Modules are loaded")
except Exception as e:
    print("Error : {} ".format(e))

browser = webdriver.Chrome()
URL = ''

browser.get(URL)
article_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
items = article_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    price = "No Price"
    img = "No Image"
    url = "No url"

    try:
        price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n",".")
    except:
        pass

    try:
        img = item.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
    except:
        pass

    try:
        url = item.find_element(By.CSS_SELECTOR, '.a-link-normal').get_attribute("href")
    except:
        pass

    print("Title: " + title)
    print("Price: " + price)
    print("Img: " + img)
    print("Url: " + url + "\n")
