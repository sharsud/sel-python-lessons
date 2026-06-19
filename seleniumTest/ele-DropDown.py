import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, UnexpectedTagNameException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/dropAlert.php")
driver.maximize_window()




# # 1. What is a Select dropdown
# # Any <select> element can be handled via Selenium's Select class
# select_element = driver.find_element(By.ID, "singleSelect")
# single_dropdown = Select(select_element)

# # 2. select_by_index(), select_by_value(), select_by_visible_text()
# single_dropdown.select_by_index(1)            # Select second option
# time.sleep(1)
# single_dropdown.select_by_value("csharp")     # Select by value
# time.sleep(1)
# single_dropdown.select_by_visible_text("Java")  # Select by visible text
# time.sleep(1)
#
# # 3. Getting all options from dropdown
# all_options = single_dropdown.options
# print("All options in dropdown:")
# for opt in all_options:
#     print(opt.text)


# # 4. Checking selected option
# selected_option = single_dropdown.first_selected_option
# print("Currently selected:", selected_option.text)

# # 5. Validating dropdown default selection
# default_selection = single_dropdown.first_selected_option.text
# print("Default selection:", default_selection)

# # 6. Handling multi-select dropdowns
# multi_element = driver.find_element(By.ID, "multiSelect")
# multi_dropdown = Select(multi_element)
#
# if multi_dropdown.is_multiple:
#     multi_dropdown.select_by_visible_text("Python")
#     multi_dropdown.select_by_value("java")
#     multi_dropdown.select_by_index(4)
#     time.sleep(1)
# time.sleep(1)
# # 7. Deselect methods (for multi-select)
# multi_dropdown.deselect_by_index(4)
# time.sleep(1)
# multi_dropdown.deselect_by_value("java")
# time.sleep(1)
# multi_dropdown.deselect_all()  # Uncomment to deselect all

# # 8. Conditional dropdown selection
# for option in multi_dropdown.options:
#     print(option.text)
#     if option.text == "JavaScript":
#         multi_dropdown.select_by_visible_text("JavaScript")
#         print("Selected JavaScript based on condition")
#         break

# # 9. Handling disabled or hidden dropdowns
# disabled_dropdown = driver.find_element(By.ID, "disbaledSelect")
# dropdown_type=disabled_dropdown.is_enabled() #false
# print(dropdown_type)
#
# val=disabled_dropdown.get_attribute("disabled") #true
# print(val)
# disabled_dropdown = driver.find_element(By.ID, "disbaledSelect")
# Select(disabled_dropdown).select_by_index(1)
#
# try:
#     disabled_dropdown = driver.find_element(By.ID, "disbaledSelect")
#     Select(disabled_dropdown).select_by_index(0)
# except ElementNotInteractableException:
#     print("Cannot interact with disabled dropdown!")

# # Common exceptions and how to avoid them:
# # - NoSuchElementException -> when element not found
# # - ElementNotInteractableException -> when element is disabled/hidden
# # - UnexpectedTagNameException -> when Select is used on a non-<select> element
#
try:
    fake_select = driver.find_element(By.ID, "submitBtn")
    Select(fake_select)
except UnexpectedTagNameException:
    print("Cannot use Select on a non-select element!")

