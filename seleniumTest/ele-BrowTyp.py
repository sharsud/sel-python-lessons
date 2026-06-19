import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from seleniumTest.Utils.highlight import highlight_flash as blink

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/BrNavBasic.php")
driver.maximize_window()


# # Element Interaction Basics
# # 	• Clicking elements (.click())
# driver.find_element(By.ID,'btnClear').click()
# # 	• Typing into inputs (.send_keys())
# driver.find_element(By.ID,'inputField').send_keys('Hello World')
# # 	• Clearing inputs (.clear())
# # time.sleep(4)
# driver.find_element(By.ID,'inputField').clear()
# # 	• Submitting forms (.submit() – when applicable)
#
# driver.find_element(By.ID, "name").send_keys("John Doe")
# driver.find_element(By.ID, "email").send_keys("john@example.com")
# driver.find_element(By.ID, "message").send_keys("Hello! This is a test.")
# driver.find_element(By.ID,'contactForm').submit()
#
# # 	• Getting element text (.text)
# submit_text=driver.find_element(By.ID,'successMessage').text
# if "Form submitted successfully!" in submit_text:
# 	print("Form submitted successfully!")
# else:
# 	print("Form submitted unsuccessfully!")
# # 	• Retrieving element attributes (.get_attribute("value"), "href", "src", etc.)
#
# url=driver.find_element(By.ID,'linkExample').get_attribute('href')
# print(url)
# # 	• Getting element CSS properties (.value_of_css_property())
# txt_color=driver.find_element(By.ID,'cssExample').value_of_css_property('font-color')
# txt_size=driver.find_element(By.ID,'cssExample').value_of_css_property('font-size')
#
# print(f"the value of font color is {txt_color}")
# print(f"the value of font size is {txt_size}")
#


#
# # State & Visibility Checks
# # 	• Check if an element is displayed (.is_displayed())
# element_state=driver.find_element(By.ID,'hiddenText').is_displayed()
# print(f"the value of hidden text is {element_state}")
# driver.find_element(By.ID,'btnShowHidden').click()
# element_state=driver.find_element(By.ID,'hiddenText').is_displayed()
# print(f"the value of hidden text is {element_state}")
#
# # 	• Check if an element is enabled (.is_enabled())
# button_state=driver.find_element(By.ID,'btnDisabled').is_enabled()
# print(f"the value of button state is {button_state}")
#
# # 	• Check if an element is selected (.is_selected() — radio/checkbox)
# chkbox=driver.find_element(By.ID,'chkAgree')
# print(chkbox.is_selected())
# driver.find_element(By.XPATH, '//label[@for="chkAgree"]').click()
# print(f"the value of chkagree is {chkbox.is_selected()}")


# Advanced Typing & Actions
# 	• Using Keys (Keys.ENTER, Keys.TAB, Keys.ARROW_DOWN, etc.)
# driver.find_element(By.ID, "message").send_keys("Hello! This is a test.")
# driver.find_element(By.ID, "message").send_keys(Keys.RETURN)
# 	• Sending keyboard shortcuts (e.g., CTRL+A, CTRL+C, CTRL+V)
# Browser Navigation Commands
# url1=driver.find_element(By.ID, "linkExample").get_attribute("href")
#
# # 	• driver.get(url) vs driver.navigate.to(url) (if comparing with Java Selenium)
# driver.get(url1)
# # 	• driver.back() – Go to previous page
# driver.back()
# # 	• driver.forward() – Go forward in history
# driver.forward()
# # 	• driver.refresh() – Refresh page
# driver.refresh()
# print(driver.current_url)



# # Scrolling & Viewport Handling
# # 	• Scroll to element using JavaScript (element.scrollIntoView())
# scroll_element=driver.find_element(By.ID, "scrollTarget")
# driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
# 	• Scroll by coordinates (window.scrollBy())
driver.execute_script("window.scrollBy(0,500);")
#
#
