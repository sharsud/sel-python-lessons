import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, UnexpectedTagNameException, StaleElementReferenceException
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

driver.find_element(By.XPATH, "//div[@class='tab-buttons']/button[2]").click()

# 1. Difference between <select> and non-select dropdowns

# # For SELECT dropdowns (use Select class)
# select_element = driver.find_element(By.ID, "singleSelect")
# select = Select(select_element)
# select.select_by_visible_text("Python")
#
# # For NON-SELECT dropdowns (custom handling)
# input_field = driver.find_element(By.ID, "autosuggest")
# input_field.send_keys("Py")


# # 2. Typing into input fields with auto-suggestions
# input_field = driver.find_element(By.ID, "autosuggest")
# input_field.send_keys("Java")


# # 3. Waiting for suggestion list to appear (Explicit Wait)
# input_field = driver.find_element(By.ID, "autosuggest")
# input_field.send_keys("Ja")
#
# # Wait for suggestions to appear
# wait = WebDriverWait(driver, 10)
# suggestions = wait.until(EC.visibility_of_element_located((By.ID, "suggestions")))
# print(suggestions.text)


# # 4. Clicking a suggestion using mouse
# input_field = driver.find_element(By.ID, "autosuggest")
# input_field.send_keys("Py")
#
# # Wait for and click specific suggestion
# suggestion = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Python')]"))
# )
# suggestion.click()

# # 5. Handling dynamic suggestion lists (AJAX-based)
# ajax_input = driver.find_element(By.ID, "ajaxAutosuggest")
# ajax_input.send_keys("Go")
#
# # Wait for AJAX results
# suggestion = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[@id='ajaxSuggestions']//div[contains(text(), 'Go')]"))
# )
# suggestion.click()
#

# For Basic Auto-Suggest:

# # Simple waiting - elements already exist
# input_field.send_keys("Py")
# suggestions = driver.find_element(By.ID, "suggestions")
# WebDriverWait(driver, 10).until(
#     EC.visibility_of(suggestions)  # Just wait for visibility
# )
# # For AJAX-Based Auto-Suggest:
# # Complex waiting - elements don't exist initially
# input_field.send_keys("Py")
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#ajaxSuggestions .suggestion-item"))
#     # Wait for elements to be CREATED and ADDED to DOM
# )





# # 6. XPath/CSS strategies for capturing suggestions
# # Various locator strategies
# suggestion1 = driver.find_element(By.XPATH, "//div[@class='suggestion-item' and text()='Python']")
# suggestion2 = driver.find_element(By.CSS_SELECTOR, ".suggestion-item[data-category='backend']")
# suggestion3 = driver.find_element(By.XPATH, "//div[contains(@class, 'suggestion-item') and contains(text(), 'Java')]")
# suggestion4 = driver.find_element(By.XPATH, "//div[@data-category='backend' and @data-popularity='high']")

# # 7. Validating selection after picking an option
# # Select an option
# input_field = driver.find_element(By.ID, "autosuggest")
# input_field.send_keys("Java")
# suggestion = driver.find_element(By.XPATH, "//li[text()='Java']")
# suggestion.click()
#
# # Validate the selection
# selected_value = input_field.get_attribute("value")
# assert selected_value == "Python", f"Expected 'Python' but got '{selected_value}'"
#
# # Or check validation message
# validation = driver.find_element(By.ID, "nonSelectValidation")
# assert "Python" in validation.text


# 8. Handling hidden or off-screen suggestions
hidden_input = driver.find_element(By.ID, "hiddenAutosuggest")
hidden_input.click()  # This reveals the hidden suggestions

# Wait for suggestions to be visible
suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='hiddenSuggestions']//div[text()='Python Programming']"))
)
suggestion.click()

# all in ONE :
# Type to trigger suggestions
complex_input = driver.find_element(By.ID, "complexAutosuggest")
complex_input.send_keys("Py")

# Wait for suggestions to appear
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "complexSuggestions"))
)

# Click Python suggestion
python_suggestion = driver.find_element(By.XPATH, "//div[@id='complexSuggestions']//div[contains(text(), 'Python')]")
python_suggestion.click()


