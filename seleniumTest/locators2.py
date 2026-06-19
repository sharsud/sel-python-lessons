import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://examples.learnwithpsudo.com/pages/webElements.php")

# driver.find_element(By.LINK_TEXT, "Click here to log in").click()

#pratial link text
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Click here").click()

# driver.find_element(By.LINK_TEXT, "HELLO, ADMIN").click()

#all links starting with hello
# links=driver.find_elements(By.PARTIAL_LINK_TEXT, "HELLO")
# for link in links:
#     print(link.text)

#find all broken links
alllinks=driver.find_elements(By.TAG_NAME, "a")
for link in alllinks:
    url=link.get_attribute("href") # extract the URL
    print(url)
    if url and url.startswith("https://"):
        try:
            response = requests.head(url, timeout=5)
            if response.status_code >=400:
                print(f"BROKEN URL : {url} -> {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"BROKEN URL EXCEPTION RAISED: {url} -> {e}")