from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from seleniumTest.Utils.highlight import highlight_flash as blink

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/xpathdemo.php")
driver.maximize_window()

#
# # ---------------------------------------------------------
# # Concept: Use 'contains()' when attribute values are partially dynamic.
# # Usage: Select elements whose attribute contains a specific substring.
# # Syntax: //tag[contains(@attribute,'partialValue')]
# # Common Mistake: Using too generic substring → can select multiple elements.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//input[contains(@id,'email')]") # selects only the first matching ele
# ele.send_keys("entered texts")
# blink(driver,ele)

# # ---------------------------------------------------------
# # Concept: Use 'starts-with()' when attribute starts with a stable prefix.
# # Usage: Ideal for dynamic IDs/names with fixed prefix.
# # Syntax: //tag[starts-with(@attribute,'prefix')]
# # Common Mistake: Prefix should be unique enough; avoid common words.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//input[starts-with(@name,'user')]")
# blink(driver,ele)


# # ---------------------------------------------------------
# # Concept: XPath 1.0 doesn't support ends-with(), use substring() workaround.
# # Usage: Match attribute values ending with a known suffix.
# # Syntax: //tag[substring(@attribute,string-length(@attribute)-N)='suffix']
# # Common Mistake: Miscalculating string length offset → incorrect matches.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//input[substring(@name,string-length(@name)-7)='_address']")
# blink(driver,ele)
#
# ele=driver.find_element(By.XPATH, "//input[ends-with(@name, '_address')]")
# blink(driver,ele)

# # ---------------------------------------------------------
# # Concept: Target elements by visible text content.
# # Usage: Use when text is stable and unique.
# # Syntax: //tag[text()='ExactText'] OR //*[contains(text(),'PartialText')]
# # Common Mistake: Extra spaces, case sensitivity → mismatch issues.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//button[text()='Login']")
# blink(driver,ele)
#
# ele=driver.find_element(By.XPATH, "//*[contains(text(),'Welcome')]")
# blink(driver,ele)

# # ---------------------------------------------------------
# # Wildcards & Multiple Attributes
# # Concept: //* matches any element; combine with multiple conditions for precision.
# # Usage: Use when tag is unknown or multiple attributes define uniqueness.
# # Syntax: //* OR //tag[@attr1='value' and @attr2='value']
# # Common Mistake: Overusing //* slows down execution and reduces accuracy.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//*")  # Matches any element
# blink(driver,ele)
#
# ele=driver.find_element(By.XPATH, "//div/*")  # Matches all children of a div
# blink(driver,ele)
#
# ele=driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Username']")
# blink(driver,ele)
#
# # ---------------------------------------------------------
# # XPath Axes
# # Concept: Navigate relative to another element using axes.
# # Usage: Use axes like following, preceding, ancestor for relational navigation.
# # Syntax: //tag[condition]/axis::targetTag
# # Common Mistake: Omitting index → selects wrong element if multiple matches exist.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]")
# blink(driver,ele)
# ele=driver.find_element(By.XPATH, "//input[@id='password']/preceding::label")
# blink(driver,ele)
# ele=driver.find_element(By.XPATH, "//input[@id='password']/ancestor::div")
# blink(driver,ele)
# ele=driver.find_element(By.XPATH, "//input[@id='password']/parent::div")
# blink(driver,ele)



# # ---------------------------------------------------------
# # chained xpath
# # Concept: Combine conditions across nested nodes for accuracy.
# # Usage: Ideal for structured layouts with multiple levels.
# # Syntax: //parentTag[@attr='value']//childTag[@attr='value']
# # Common Mistake: Forgetting '//' before child selector → no match.
# # ---------------------------------------------------------
#
# ele=driver.find_element(By.XPATH, "//div[@class='container']//input[@name='email']")
# blink(driver,ele)

# ---------------------------------------------------------
# tables
# Concept: Locate data in rows and columns using tr/td hierarchy.
# Usage: Use row & column indexes or loop with find_elements().
# Syntax: //table/tbody/tr[n]/td[m]
# Common Mistake: Hardcoding indexes → fragile when table changes dynamically.
# ---------------------------------------------------------

ele=driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[1]")  # Bob
blink(driver,ele)
ele=driver.find_element(By.XPATH, "//table//tr[position()=3]/td[2]")  # Charlie's Age
blink(driver,ele)


