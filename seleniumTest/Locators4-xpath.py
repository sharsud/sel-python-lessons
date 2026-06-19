from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from seleniumTest.Utils.highlight import highlight_flash as blink

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/xpathdemo.php")
driver.maximize_window()

# Absolute XPath
# - Starts from the root (/html/body/...) and navigates step-by-step
# - Fragile: breaks with even small changes in HTML structure
# - Use for quick testing only, not in real scripts
ele=driver.find_element(By.XPATH, "html/body/div/article/section/div/div[1]/input")
ele.send_keys("entered texts")

# blink(driver, ele)

# Relative XPath
# - Starts with //, searches from anywhere in the DOM
# - Flexible and preferred in real-world automation
ele= driver.find_element(By.XPATH, "//input[@id='relativeField']")
blink(driver, ele)



# Basic XPath Syntax
# - //tagname[@attribute='value']
ele= driver.find_element(By.XPATH, "//input[@id='emailFromLabel']")
blink(driver, ele)
# - //* [text()='Login']
ele=driver.find_element(By.XPATH, "//*[text()='Login']")
blink(driver, ele)
# - Combine conditions with 'and'
ele=driver.find_element(By.XPATH, "//input[@type='email' and @name='email']")
blink(driver, ele)




# Text-based XPath
# - Useful when elements don’t have ID or class but have static visible text
ele=driver.find_element(By.XPATH, "//button[text()='Submit']")
blink(driver, ele)
ele=driver.find_element(By.XPATH, "//*[text()='Reset Fields']")
blink(driver, ele)

# Indexing & Position
# - Used when no unique attribute is available
# - (//input)[2] selects the second input on the page
ele=driver.find_element(By.XPATH, "(//input)[3]")
blink(driver, ele)
# - //input[position()=3] selects the third input in its parent
ele=driver.find_element(By.XPATH, "//input[position()=3]")
blink(driver, ele)
#
# # XPath Use Cases
# # - Forms without IDs
# # - Modal dialog buttons
# # - Reading values from tables
# # - Selecting dropdown items or list elements