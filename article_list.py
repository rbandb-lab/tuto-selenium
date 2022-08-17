import json
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

try:
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    print("All Modules are loaded")
except Exception as e:
    print("Error : {} ".format(e))

# create a file from an empty array to store elements
file_path = Path(__file__).parent / "./data.json"

if os.path.exists(file_path):
    os.remove(file_path)

Path(file_path).touch()
with open(file_path, "r+") as f:
    json.dump([], f)
print("Created data.json file at path " + str(file_path))

def push_json(new_data, filename=file_path):
    with open(filename, "r+") as f:
        file_content = json.load(f)
        file_content.append(new_data)
        f.seek(0)
        json.dump(file_content, f, indent=4)


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

        push_json([
            "Title: " + title,
            "Price: " + price,
            "Img: " + img,
            "Url: " + url + "\n"
        ])


url = 'https://www.amazon.com/s?k=Ryzen+AMD+processor&rh=n%3A172282%2Cp_89%3AAMD&dc&ds=v1%3ABSaG4inkaIHjdsrbs6HeSwEGbnZzOmvWJV1pq1E5PPY&qid=1660759417&rnid=2528832011&ref=sr_nr_p_89_1'
hasNextPageDisabled = False
browser.get(url)

while not hasNextPageDisabled:
    next_btn = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 's-pagination-next')))
    articles(browser)
    next_class = next_btn.get_attribute('class')
    if 'disabled' in next_class:
        hasNextPageDisabled = True
        break
    browser.find_element(By.CLASS_NAME, 's-pagination-next').click()



