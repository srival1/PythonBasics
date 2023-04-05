from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("be")
time.sleep(3) # did not remove this explicit sleep stmt as elements would take sometime to load,
# but selenium will not check if below resultslist is empty or not. Therefore, implicit wait will not work
resultslist = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(resultslist))
assert len(resultslist) != 0

for result in resultslist:
    #Chain Locator i.e. starting the line with result. instead of driver. , therefore limiting the search only to elements list
    #result.find_element(By.XPATH, "div/button").click()
    result.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5)

assert driver.find_element(By.CLASS_NAME, "promoInfo").text == 'Code applied ..!'

driver.close()

