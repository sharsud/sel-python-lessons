# This script demonstrates various strategies for locating and interacting with iframes using Selenium WebDriver in Python.
# key methods covered include:
# - switch_to.frame(), switch_to.default_content(), switch_to.parent_frame()
# - Locating iframes by ID, Name, Index, and WebElement
# - Switching between frames and main content
# - Handling nested frames with multiple levels
# - Real-world use cases like forms and widgets within frames
# - Dealing with dynamic frames that load after user interaction
# - Best practices for using explicit waits with frames
# - Troubleshooting common issues like NoSuchFrameException and NoSuchElementException
from selenium import webdriver
from selenium.common import NoSuchElementException, NoSuchFrameException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumTest.Utils.highlight import highlight_flash

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/iframes.php")
driver.maximize_window()
driver.implicitly_wait(5)

# 1. LOCATING IFRAMES - Different Strategies
print("=== 1. Locating iFrames ===")

# By ID
frame_by_id = driver.find_element(By.ID, "mainFrame")
print("✓ Found frame by ID")

# By Name
frame_by_name = driver.find_element(By.NAME, "sidebarFrame")
print("✓ Found frame by Name")

# By Index (0-based)
frames_by_tag = driver.find_elements(By.TAG_NAME, "iframe")
print(f"✓ Found {len(frames_by_tag)} iframes total")

# By WebElement
frame_element = driver.find_element(By.CSS_SELECTOR, "iframe.simple-frame")
print("✓ Found frame by CSS selector")

# By Index (0-based)
frames_by_tag = driver.find_elements(By.TAG_NAME, "iframe")
totIframe = len(frames_by_tag)
print(f"✓ Found {totIframe} iframes total")

for i, frame in enumerate(frames_by_tag):
    print(f"  - Frame {i} ID: {frame.get_attribute('id')}, Name: {frame.get_attribute('name')}")
    highlight_flash(driver, frame)

# 2. SWITCHING FRAMES - Basic Switching
print("\n=== 2. Switching Frames ===")

# Switch by ID---------------------------------
driver.switch_to.frame("mainFrame")
print("✓ Switched to frame by ID")

# Interact with elements inside frame
input_field = driver.find_element(By.ID, "username")
input_field.send_keys("Selenium User")
print("✓ Typed in frame input")

# Return to main content
driver.switch_to.default_content()
print("✓ Returned to main content")

# Switch by Name---------------------------------
driver.switch_to.frame("sidebarFrame")
select_element = driver.find_element(By.ID, "theme")
Select(select_element).select_by_index(1)
print("✓ Clicked select in named frame")

driver.switch_to.default_content()

# Switch by Index--------------------------
driver.switch_to.frame(2)  # Third iframe (0-based index)
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()
print("✓ Clicked checkbox in frame by index")

driver.switch_to.default_content()


# Switch by WebElement-locators--------------------------
frame = driver.find_element(By.XPATH, "//*[@id='mainFrame']")
driver.switch_to.frame(frame)
print("✓ Switched to frame by WebElement")
driver.switch_to.default_content()


# 3. NESTED FRAMES - Multiple Levels
print("\n=== 3. Nested Frames ===")

# Switch to parent frame with wait
parent_frame = WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it("parentFrame")
)
print("✓ Switched to parent frame")

# Wait for element in parent frame
parent_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "parentInput"))
)
parent_input.send_keys("Text in parent frame")
print("✓ Typed in parent frame")

# Switch to child frame with wait
child_frame = WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it("childFrame")
)
print("✓ Switched to child frame")

# Wait for button in child frame
child_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Child Button')]"))
)
child_button.click()
print("✓ Clicked button in child frame")

# Wait for grandchild frame to be available
grandchild_frames = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
)
print(f"✓ Found {len(grandchild_frames)} frames in child level")

if grandchild_frames:
    # Switch to grandchild frame (first iframe in child frame)
    driver.switch_to.frame(grandchild_frames[0])
    print("✓ Switched to grandchild frame")

    # Wait for email field in grandchild frame
    grandchild_email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "grandchildEmail"))
    )
    grandchild_email.send_keys("test@example.com")
    print("✓ Typed email in grandchild frame")

    # Navigate back up the hierarchy
    driver.switch_to.parent_frame()  # Back to child
    print("✓ Back to child frame")
else:
    print("✗ No grandchild frame found")

driver.switch_to.parent_frame()  # Back to parent
driver.switch_to.default_content()  # Back to main
print("✓ Back to main content")

# 4. REAL-WORLD USE CASES
print("\n=== 4. Real-world Use Cases ===")

# Contact Form Frame
driver.switch_to.frame("contactFormFrame")
name_field = driver.find_element(By.ID, "name")
name_field.send_keys("John Doe")
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("john@example.com")
message_field = driver.find_element(By.ID, "message")
message_field.send_keys("Test message from Selenium")
print("✓ Filled contact form in frame")

driver.switch_to.default_content()

# Map Widget Frame
driver.switch_to.frame("mapWidgetFrame")
search_field = driver.find_element(By.ID, "searchLocation")
search_field.send_keys("New York")
print("✓ Searched location in map widget")

driver.switch_to.default_content()

# 5. DYNAMIC FRAMES
print("\n=== 5. Dynamic Frames ===")

# Click to load dynamic frame
load_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load Dynamic iFrame')]")
load_button.click()

# Wait for dynamic frame to load
dynamic_frame = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dynamicFrame"))
)

driver.switch_to.frame("dynamicFrame")
dynamic_input = driver.find_element(By.ID, "dynamicNumber")
dynamic_input.send_keys("123")
dynamic_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Dynamic Button')]")
dynamic_button.click()
print("✓ Interacted with dynamic frame")

driver.switch_to.default_content()

# 6. BEST PRACTICES - Explicit Waits with Frames
print("\n=== 6. Best Practices with Waits ===")

# Wait for frame to be available and switch to it
frame = WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it("mainFrame")
)

# Wait for element inside frame
element_in_frame = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username"))
)
element_in_frame.clear()
element_in_frame.send_keys("Text with explicit wait")
print("✓ Used explicit waits with frame")

driver.switch_to.default_content()

# 7. TROUBLESHOOTING - Error Handling
print("\n=== 7. Troubleshooting ===")

# Handle frame not found
try:
    driver.switch_to.frame("nonExistentFrame")
except NoSuchFrameException:
    print("✓ Caught NoSuchFrameException - frame doesn't exist")

# Handle element not found in frame
try:
    driver.switch_to.frame("mainFrame")
    driver.find_element(By.ID, "nonExistentElement")
except NoSuchElementException:
    print("✓ Caught NoSuchElementException - element not found in frame")

driver.switch_to.default_content()

# 8. COMPLETE WORKFLOW EXAMPLE
print("\n=== 8. Complete Workflow ===")


def complete_frame_workflow():
    # Start from main content
    driver.switch_to.default_content()

    # Work with first frame
    driver.switch_to.frame("mainFrame")
    driver.find_element(By.ID, "username").send_keys("Workflow Test")
    driver.find_element(By.XPATH, "//button").click()

    # Back to main, then to another frame
    driver.switch_to.default_content()
    driver.switch_to.frame("sidebarFrame")
    driver.find_element(By.ID, "theme").click()

    # Always end back in main content
    driver.switch_to.default_content()
    print("✓ Complete workflow executed successfully")


complete_frame_workflow()

print("\n=== All iFrame demonstrations completed successfully! ===")