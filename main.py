from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    print("All Modules are loaded")
except Exception as e:
    print("Error : {} ".format(e))

browser = webdriver.Chrome()

def articles(browser):
    article_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
    items = article_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

    for item in items:
        title = item.find_element(By.TAG_NAME, 'h2').text
        price = "No Price"
        img = "No Image"
        url = "No url"

        try:
            price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
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


url = 'https://www.amazon.com/s?k=Ryzen+AMD+processor&rh=n%3A172282%2Cp_89%3AAMD&dc&ds=v1%3ABSaG4inkaIHjdsrbs6HeSwEGbnZzOmvWJV1pq1E5PPY&qid=1660759417&rnid=2528832011&ref=sr_nr_p_89_1'
hasNextPageDisabled = False
browser.get(url)

while not hasNextPageDisabled:
    next_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 's-pagination-next')))
    articles(browser)
    next_class = next_btn.get_attribute('class')
    if 'disabled' in next_class:
        hasNextPageDisabled = True
        break
    browser.find_element(By.CLASS_NAME, 's-pagination-next').click()



