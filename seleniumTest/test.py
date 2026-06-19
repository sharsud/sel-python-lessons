from concurrent.futures import ThreadPoolExecutor, as_completed

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# === CONFIG ===
ROOM_URL = "https://www.drawasaurus.org/"
MESSAGE = "Hello from Selenium!"
NUM_TIMES = 5       # how many times to send
DELAY_BETWEEN = 2   # seconds between sends

# === SETUP ===

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# Mute audio
chrome_options.add_argument("--mute-audio")

# Disable extensions/plugins
chrome_options.add_argument("--disable-extensions")

# Disable plugin discovery
chrome_options.add_argument("--disable-plugins-discovery")

# Disable notifications
chrome_options.add_argument("--disable-notifications")

# Disable popup blocking
chrome_options.add_argument("--disable-popup-blocking")

# Optional performance options
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
chrome_options.add_argument("--headless=new")

driver=webdriver.Chrome()
driver.get(ROOM_URL)
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, '//*[@id="accept-choices"]').send_keys(MESSAGE)
def login(driver):
    driver.find_element(By.XPATH, '//*[@id="accept-choices"]').click()
    driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div/div[1]/form/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div/div[1]/form/div/input').send_keys("a 4 aandless")

    driver.find_element(By.XPATH, '//*[@id="modal"]//button').click()

def open_link(link):
    driverx = webdriver.Chrome(options=chrome_options)
    driverx.get(link)
    login(driverx)
    for i in range(300):
        # driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys("dobara")
        driverx.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(
            " A madarchor Arvind ki maa chude ghar ghar.. khude land par ... apni maa ke sath chudwa le.. looser asfuck bhosdiwale    ")
        driverx.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(
            Keys.ENTER)
        # time.sleep(.5)
        print(i)
        driverx.get(link)

login(driver)
elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div[2]/a')
links = [element.get_attribute("href") for element in elements]


drivers = []
with ThreadPoolExecutor(max_workers=1) as executor:
    futures = [executor.submit(open_link, link) for link in links]

    for future in futures:
        drivers.append(future.result())




