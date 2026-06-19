import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, UnexpectedTagNameException, StaleElementReferenceException, \
    TimeoutException, NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/dropAlert.php")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//div[@class='tab-buttons']/button[3]").click()

# 1. Identifying JavaScript alerts, confirms, and prompts
# Locate alert buttons
alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Confirm')]")
prompt_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Prompt')]")

print("Alert button found:", alert_button.is_displayed())
print("Confirm button found:", confirm_button.is_displayed())
print("Prompt button found:", prompt_button.is_displayed())

# # 2. Switching to alert using driver.switch_to.alert
# # Click alert button and switch to alert
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
#
# # Switch to the alert
# alert = driver.switch_to.alert
# print("Switched to alert successfully")
# time.sleep(3)
# # Don't forget to accept it
# alert.accept()

# 3. Accepting an alert using .accept()
# Simple alert - accept
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
#
# alert = driver.switch_to.alert
# alert.accept()
# print("Alert accepted")

# # Confirm box - accept
# confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Confirm')]")
# confirm_button.click()
#
# alert = driver.switch_to.alert
# time.sleep(2)
# alert.accept()
# print("Confirm box accepted - chose OK")
# alert = driver.switch_to.alert
# print(f"Confirm box message: {alert.text}")
# time.sleep(2)
# alert.accept()


# # 4. Dismissing a confirm box using .dismiss()
# # Confirm box - dismiss
# confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Confirm')]")
# confirm_button.click()
#
# alert = driver.switch_to.alert
# time.sleep(2)
# alert.dismiss()
# print("Confirm box dismissed - chose Cancel")
#
# alert = driver.switch_to.alert
# print(f"Confirm box message: {alert.text}")
# time.sleep(2)
# alert.accept()


# # 5. Sending input text to prompt pop-up using .send_keys()
# # Prompt box - send text
# prompt_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Prompt')]")
# prompt_button.click()
#
# alert = driver.switch_to.alert
# alert.send_keys("Selenium Test Input")
# time.sleep(2)
# alert.accept()
# print("Text sent to prompt and accepted")
# print(f"Prompt box message: {alert.text}")
# alert.accept()
#
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
# try:
#     alert = driver.switch_to.alert
#     print("Alert found with text:", alert.text)
#     alert.accept()
# except NoAlertPresentException:
#     print("No alert present - this is expected")


#
# # 6. Handle alert with specific actions || check the text before accepting/dismissing
# # Simple alert handling with text check
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
#
# try:
#     alert = driver.switch_to.alert
#     if "simple alert" in alert.text.lower():
#         alert.accept()
#         print("Simple alert handled")
#     else:
#         print("Unexpected alert text:", alert.text)
#         alert.dismiss()
# except NoAlertPresentException:
#     print("Failed to switch to alert")
#
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
#
# try:
#     alert = driver.switch_to.alert
#     if "sim alert" in alert.text.lower():
#         alert.accept()
#         print("Simple alert handled")
#     else:
#         print("Unexpected alert text:", alert.text)
#         alert.dismiss()
# except NoAlertPresentException:
#     print("Failed to switch to alert")
#
# # alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# # alert_button.click()
#
# try:
#     alert = driver.switch_to.alert
#     if "simple alert" in alert.text.lower():
#         alert.accept()
#         print("Simple alert handled")
#     else:
#         print("Unexpected alert text:", alert.text)
#         alert.dismiss()
# except NoAlertPresentException:
#     print("Failed to switch to alert")


# 7. Robust alert handling with multiple checks and exception handling
# Confirm box handling with timeout and exception handling
confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Confirm')]")
confirm_button.click()

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    if "confirm" in alert.text.lower():
        alert.dismiss()
        print("Confirm box dismissed")
    else:
        alert.accept()
except TimeoutException:
    print("Alert did not appear within timeout")
except NoAlertPresentException:
    print("Alert disappeared unexpectedly")
alert = driver.switch_to.alert
alert.accept()
# confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Confirm')]")
# confirm_button.click()

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    if "confirm" in alert.text.lower():
        alert.dismiss()
        print("Confirm box dismissed")
    else:
        alert.accept()
except TimeoutException:
    print("Alert did not appear within timeout")
except NoAlertPresentException:
    print("Alert disappeared unexpectedly")