#find element vs find elements
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
search_box=driver.find_element(By.ID,"firstName")
print(type(search_box))
# time.sleep(5)
# search_box.send_keys("Psudo")


# search_boxes=driver.find_elements(By.ID,"firstName")
# # time.sleep(5)
# print(type(search_boxes))
# # search_box.send_keys("Psudo2")

search_boxes=driver.find_elements(By.CLASS_NAME, "field")
print(len(search_boxes))


## no such element: Unable to locate element: {"method":"css selector","selector":"[id="firstname"]"}
# search_box=driver.find_element(By.ID,"firstname")

search_boxes=driver.find_elements(By.CLASS_NAME, "field1")
print(search_boxes)

search_boxes1=driver.find_elements(By.CLASS_NAME, "field")
# for search_box in search_boxes1:
#     print(search_box.text)

print(search_boxes1[2].text)