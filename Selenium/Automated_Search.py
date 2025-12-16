from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.barcodelookup.com/")
time.sleep(2)
search_box = driver.find_element(By.NAME, "search-input")
search_box.send_keys("8901719101038")
search_box.send_keys(Keys.RETURN)

time.sleep(25)
driver.quit()