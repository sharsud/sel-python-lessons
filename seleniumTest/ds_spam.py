from concurrent.futures import ThreadPoolExecutor, as_completed

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# === CONFIG ===
ROOM_URL = "https://www.drawasaurus.org/room/The+puppy+Room"
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

chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
chrome_options.add_argument("--headless=new")

driver=webdriver.Chrome(options=chrome_options)
driver.get(ROOM_URL)
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, '//*[@id="accept-choices"]').send_keys(MESSAGE)

driver.find_element(By.XPATH, '//*[@id="accept-choices"]').click()
driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div/div[1]/form/label/span').click()
driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div/div[1]/form/div/input').send_keys("A 4 aandless")

driver.find_element(By.XPATH, '//*[@id="modal"]//button').click()
# wait for page to load and user to join room manually

'//*[@id="__next"]/div/div/main/div/div[2]/div[2]/a'


for i in range(300):
        # driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys("dobara")
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(
             "A ki maa chude ghar ghar.. a khude land par ... apni maa ke sath chudwa le.. looser asfuck        ")
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(Keys.ENTER)
        # time.sleep(.5)
        print(i)
        driver.get(ROOM_URL)


# driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(
#          "kaisa laga mera mazak")
# driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(Keys.ENTER)

print("Please join the room and make sure chat is visible...")


#
#
# # Use 5–7 threads (pick one)
# chrome_options = Options()
# # chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless=new")  # modern headless mode
# chrome_options.add_argument("--disable-gpu")
#
# driver = webdriver.Chrome(options=chrome_options)
# MAX_THREADS = 20
# driver.get(ROOM_URL)
# driver.implicitly_wait(10)
#
# driver.find_element(By.XPATH, '//*[@id="accept-choices"]').click()
# driver.find_element(By.XPATH,'//*[@id="modal"]/div/div/div/div[1]/form/label/span').click()
# driver.find_element(By.XPATH,'//*[@id="modal"]/div/div/div/div[1]/form/div/input').send_keys("admin")
# driver.find_element(By.XPATH, '//*[@id="modal"]//button').click()
# for _ in range(100):
#     driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys("Mai pagal hu")
#     driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div[3]/div[2]/form/input').send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/header/a').click()
#     driver.get(ROOM_URL)
#
#
