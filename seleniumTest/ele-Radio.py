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

# # ------------------------
# # 1. Check if Selected – is_selected()
# # ------------------------
# gender_male = driver.find_element(By.ID, "genderMale")
# # gender_male.click()
# # driver.execute_script("arguments[0].click()", gender_male)
# driver.find_element(By.CSS_SELECTOR, "label[for='genderFemale']").click()
# print("Is Male selected?", gender_male.is_selected())
# #
# # ------------------------
# # 2. Select Only if Not Selected
# # ------------------------
# if not gender_male.is_selected():
#     driver.find_element(By.CSS_SELECTOR, "label[for='genderMale']").click()

# # ------------------------
# # 3. Loop Through a Radio Button Group
# # ------------------------
radios = driver.find_elements(By.NAME, "gender")
# for radio in radios:
#     if radio.get_attribute("value") == "female":
#         radio.click() # replace this with label.click
#         break

# # ------------------------
# # 4. Pre-selected Radio Button Verification
# # ------------------------
# for radio in radios:
#     if radio.is_selected():
#         print("Pre-selected gender:", radio.get_attribute("value"))
#
# # ------------------------
# # 5. Select by Label Text
# # ------------------------
# labels = driver.find_elements(By.TAG_NAME, "label")
# for lbl in labels:
#     if lbl.text.strip() == "Other":
#         lbl.click()
#         break
# time.sleep(2)
# # ------------------------
# # 6. Disabled Radio Buttons
# # ------------------------
# disabled_radio = driver.find_element(By.ID, "disabledRadio")
# print("Is disabled radio enabled?", disabled_radio.is_enabled())  # Should be False
#

# ------------------------
# 7. Lazy / Delayed Elements (Scroll into view)
# ------------------------

lazy_radio = driver.find_element(By.ID, "lazyRadio")

# driver.execute_script("arguments[0].click();", lazy_radio)
driver.execute_script("arguments[0].scrollIntoView();", lazy_radio)
time.sleep(0.5)  # wait for the animation/delay
driver.find_element(By.CSS_SELECTOR, "label[for='lazyRadio']").click()


# ------------------------
# 8. Form Validation Example (Check selection before submitting)
# ------------------------
selected_radio = None
for radio in radios:
    if radio.is_selected():
        selected_radio = radio.get_attribute("value")

if selected_radio:
    print("Ready to submit, selected gender:", selected_radio)
else:
    print("No radio selected, cannot submit")

# ------------------------
# 9. Error Handling Example
# ------------------------
try:
    lazy_radio.click()
except ElementNotInteractableException:
    print("Lazy radio not interactable!")
except StaleElementReferenceException:
    print("Element went stale!")

# ------------------------
# 10. Business Rule Example (Select Male if available)
# ------------------------
for radio in radios:
    if radio.get_attribute("value") == "male" and radio.is_enabled():
        # Get the ID of the radio
        radio_id = radio.get_attribute("id")
        # Find the associated label using the 'for' attribute
        label = driver.find_element(By.CSS_SELECTOR, f"label[for='{radio_id}']")
        label.click()
        print("Business rule applied: Male selected")
        break