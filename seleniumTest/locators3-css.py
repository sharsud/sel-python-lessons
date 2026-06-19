from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/classLocatorsdemo.php")

# 1. ID Selector
# Use when the element has a unique ID.
# Format: Use '#' followed by the ID.
# Good for fields like username, password, and buttons with static IDs.

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Psudo")

# 2. Class Selector
# Use when elements share a common class.
# Format: Use '.' before the class name.
# Useful for targeting input fields, buttons, or divs with common styles.

email=driver.find_elements(By.CSS_SELECTOR, ".input-email")
email[0].send_keys("learnwithpsudo@gmail.com")
email[1].send_keys("learnwithpsudo@gmail.com")

# 3. Tag and Attribute Selector
# Combines the tag with a specific attribute value.
# Format: tag[attribute='value']
# Ideal when elements have stable placeholder, name, or type attributes.

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter password']").send_keys("Password1")

# 4. Tag and Class Combo
# Targets a specific tag with a specific class.
# Format: tag.className (no space between them)
# Best used when the same class is applied to multiple tags.

driver.find_element(By.CSS_SELECTOR, "textarea.input-field").send_keys("this is a class and tag combo")

# 5. Descendant Selector
# Used to find an element nested anywhere inside another element.
# Format: parent child (with a space between them)
# Effective for locating deep-nested elements like radio buttons or labels inside divs.

driver.find_element(By.CSS_SELECTOR, "div.field.group-block label[for='langPython']").click()

# 6. Starts With Attribute Selector
# Selects elements whose attribute starts with a specific value.
# Format: tag[attribute^='prefix']
# Useful for dynamic fields with predictable starting text like user_name, user_id.

driver.find_element(By.CSS_SELECTOR, "input[name^='user']").send_keys("startsWithuser")

# 7. Ends With Attribute Selector
# Selects elements whose attribute ends with a specific value.
# Format: tag[attribute$='suffix']
# Ideal for fields like first_name, last_name, email_id.

driver.find_element(By.CSS_SELECTOR, "input[name$='name']").send_keys("EndsWithuser")

# 8. Contains Attribute Selector
# Matches elements whose attribute contains a specific value anywhere.
# Format: tag[attribute*='value']
# Helpful when attribute values are dynamic but contain a consistent keyword.
driver.find_element(By.CSS_SELECTOR, "textarea[placeholder*='feedback']").send_keys("this is a feedback received!!")


# 9. Nested Selectors
# For targeting elements in complex layouts.

# Descendant Selector
# Selects any child at any depth inside a parent.
# Format: parent child
# Great for inputs inside cards, sections, or modals.

# Direct Child Selector
# Selects only immediate children, not grandchildren.
# Format: parent > child
# Best used when the structure is fixed and predictable.

fields=driver.find_elements(By.CSS_SELECTOR, "form>.fields>.field")
print(len(fields))

# [Common Mistakes to Avoid]
# 	• Don’t use space where dot (.) is needed in class combos
# 	• Don’t forget: #id, .class, [attr='value'] — no quotes inside CSS unless for attribute values
# 	• Don’t mix XPath syntax with CSS selectors — it’s like mixing Pepsi with chai. Doesn’t work.
#
# [Best Practices Recap]
# ✔ Use CSS selectors when id is missing
# ✔ They are generally faster than XPath
# ✔ Keep them short, clean, and readable
# ✔ Use attribute patterns (^=, *=, $=) when dynamic values are present

# Multiple Classes
# When matching multiple classes, chain them without spaces.
# Format: .class1.class2

# nth-of-type
# Selects an element based on its position in the parent.
# Format: tag:nth-of-type(n)
# Useful for picking specific elements like the 3rd input in a group (e.g., OTP fields).
driver.find_element(By.CSS_SELECTOR, ".field:nth-of-type(2) input").send_keys("this is nth child two")