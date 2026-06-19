"""
🔹 ID
🔹 Name
🔹 Class Name
🔹 Tag Name
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
"""
ID – Most Reliable & Fastest
IDs are: Fast, Unique, very stable (if not dynamically generated)
But:
    Not all elements have an ID
    Some IDs are dynamically generated and can change every time the page loads"
"""
driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")
firstName=driver.find_element(By.ID, "firstNasme")
firstName.send_keys("Psudo")
lastName=driver.find_element(By.ID, "lastName")
lastName.send_keys("QA")
"""
Name – Common in Forms
When to use Name: When there's no ID available
It's commonly used in login forms, signup pages, etc.
if there are multiple elements with the same name, Selenium will only pick the first one."

"""

driver.find_element(By.NAME, "email").send_keys("learnwithpsudo@gmail.com")


"""

The Class Name locator can be helpful — but it has some limitations
If the element has multiple class names, like: <input class="form-input rounded bold" />
Then By.CLASS_NAME won’t work as expected, because it expects only one class name, not the whole string. Use css selector

"""

# fieldNames=driver.find_elements(By.CLASS_NAME, "fields")
# for field in fieldNames:
#     print(field.text)
# #use class name

divtag=driver.find_element(By.CLASS_NAME, "field")
txtField=divtag.find_element(By.TAG_NAME, "input")
txtField.clear()
txtField.send_keys("learnwithpsudo@gmail.com")


#loop and find elements


#



"""
It’s rarely used on its own — but super helpful when paired with other strategies or loops
"""

# #add text in first text box
# links=driver.find_elements(By.TAG_NAME, "a")
# for link in links:
#     print(link.text)
#
#
# #loop to check runtime values


