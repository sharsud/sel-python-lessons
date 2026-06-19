# import selenium
# print(selenium.__version__)
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.learnwithpsudo.com")
driver.maximize_window()
time.sleep(5)
# driver.quit()