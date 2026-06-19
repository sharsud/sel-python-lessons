from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from seleniumTest.Utils.highlight import highlight_flash as blink

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/relativeLoc.php")
driver.maximize_window()


#  # Using above()
# 	# • Locate a field above a reference element.
# 	# • Example: Find the "Password" label above Email input.
#
# email_input=driver.find_element(By.ID, "emailInput")
# email_lable=driver.find_element(locate_with(By.TAG_NAME, "label").above(email_input))
# print(f"The lable above the email field is : {email_lable.text}")
# blink(driver,email_lable)
#
#
#  # Using below()
# 	# • Locate input below a specific label.
# 	# • Example: Find Email input below "Password" label.
#
# email_input = driver.find_element(By.ID, "emailInput")
# password_input = driver.find_element(locate_with(By.TAG_NAME, "input").below(email_input))
# password_input.send_keys("my_secure_password")
# blink(driver,password_input)
#
#
#  # Using toLeftOf()
# 	# • Locate elements in horizontal layouts.
# 	# • Example: Select "Sibling 1" input to the left of "Sibling 2".
#
# right_input = driver.find_element(By.ID, "siblingRight")
# left_input = driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(right_input))
# left_input.send_keys("I'm left of sibling")
# blink(driver,left_input)
#
#  # Using toRightOf()
# 	# • Similar to left, but right alignment.
# 	# • Example: Find "Sibling 2" input to the right of "Sibling 1".
# left_input = driver.find_element(By.ID, "siblingLeft")
# right_input = driver.find_element(locate_with(By.TAG_NAME, "input").to_right_of(left_input))
# right_input.send_keys("I'm right of sibling")
# blink(driver, right_input)
#
#
#  # Using near()
# 	# • Locate elements near another (within ~50px).
# 	# • Use case: Buttons near other text fields.
# near_ref = driver.find_element(By.ID, "nearRef")
# near_button = driver.find_element(locate_with(By.TAG_NAME, "button").near(near_ref))
# blink(driver,near_button)
# near_button.click()
#


 # Combining Relative Locators
	# • Chain multiple conditions: below() + toRightOf().
	# • Use case: Locate dynamic fields in complex layouts.

# email_input = driver.find_element(By.CSS_SELECTOR, "emailInput")
# email_label = driver.find_element(locate_with(By.TAG_NAME, "label").above(email_input))
# element = driver.find_element(
#     locate_with(By.TAG_NAME, "input")
#     .below(email_label)
#     .toRightOf(near_button)
# )
# label_left=driver.find_element(By.CSS_SELECTOR, "label[for='nearRef']")
# btn_right=driver.find_element(By.ID, "btnNear")
# field_selected=driver.find_element(locate_with(By.TAG_NAME, "input").to_right_of(label_left).to_left_of(btn_right))
# blink(driver,field_selected)



"""Best Practices:
• Use relative locators for temporary locators like onboarding screens.
• Combine with wait.until() for dynamic elements.
• Avoid over-chaining; too many .toLeftOf().near().below() calls can confuse you more than help 😅
"""