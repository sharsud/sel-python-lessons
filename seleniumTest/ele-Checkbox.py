import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from seleniumTest.Utils.highlight import highlight_flash as blink

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/chkboxdemo.php")
driver.maximize_window()
#
# # 1. Check if Selected – Use is_selected()
# print("------------Check if Selected – Use is_selected()-----------------------\n")
# # Check if "Subscribe to Newsletter" checkbox is selected
# checkbox = driver.find_element(By.ID, "chk_news")
# print(checkbox.is_selected())  # True or False
#
#
#
# # 2. Select Only if Not Selected
# print("------------Select Only if Not Selected-----------------------\n")
# checkbox = driver.find_element(By.ID, "chk_news")
# if not checkbox.is_selected():
#     # checkbox.click()
#     driver.find_element(By.CSS_SELECTOR, "label[for='chk_news']").click()
# time.sleep(3)
# print(checkbox.is_selected())
#
#
#
# # 3. Unselect Only if Selected
# print("------------Unselect Only if Selected-----------------------\n")
# checkbox = driver.find_element(By.ID, "chk_news")
# if checkbox.is_selected():
#     driver.find_element(By.CSS_SELECTOR, "label[for='chk_news']").click()
# print(checkbox.is_selected())
#
#
#
#
#
# # 4. Loop Through Grouped Checkboxes
# # Loop through checkboxes with class 'grouped' and select all
# print("------------Loop Through Grouped Checkboxes-----------------------\n")
# grouped_checkboxes = driver.find_elements(By.CSS_SELECTOR, ".grouped")
# for cb in grouped_checkboxes:
#     checkbox_id = cb.get_attribute("id")
#     if checkbox_id and not cb.is_selected():
#         label = driver.find_element(By.CSS_SELECTOR, f"label[for='{checkbox_id}']")
#         print(label.text)
#         label.click()
#
#
#
#
# # 5. Handle Disabled Checkboxes
# print("------------Handle Disabled Checkboxes-----------------------\n")
# # Suppose we had a disabled checkbox (not in current HTML, example)
# disabled_cb = driver.find_element(By.ID, "disabledCheckbox")
# print(f"the lable's isenabled() is : {disabled_cb.is_enabled()}")





# 6. Dynamic / Lazy Loaded Checkboxes
print("------------Dynamic / Lazy Loaded Checkboxes-----------------------\n")
lazy_checkbox = driver.find_element(By.ID, "lazyChk")
print(lazy_checkbox.is_displayed())
# Scroll into view
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "lazySection"))
# Click after it appears
lazy_checkbox = driver.find_element(By.ID, "lazyChk")
print(lazy_checkbox.is_displayed())
driver.find_element(By.CSS_SELECTOR, "label[for='lazyChk']").click()





# 7. Form Validation – Check Before Submission
print("------------Form Validation – Check Before Submission-----------------------\n")
checkbox = driver.find_element(By.ID, "chk_terms")
if checkbox.is_selected():
    driver.find_element(By.ID, "submitBtn").click()
else:
    print("Please agree to terms before submitting")