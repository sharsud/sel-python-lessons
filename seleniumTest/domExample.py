import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.wikipedia.org/")
search_box=driver.find_element(By.ID,"searchInput")
time.sleep(5)
search_box.send_keys("selenium")