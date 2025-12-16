from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nilesh-g.github.io/learn-web/HTML/demo08.html")
driver.implicitly_wait(10)
list = driver.find_elements(By.TAG_NAME, "li")
for item in list:
    print(item.text)
for item in list:
    with open('Headless_Search.txt', 'a') as f:
        f.write(item.text + '\n')

driver.quit()