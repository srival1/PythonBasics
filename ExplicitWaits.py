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
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

expectedlist = ["Cucumber - 1 Kg", "Beetroot - 1 Kg", "Beans - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actuallist = []
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("be")
time.sleep(3) # did not remove this explicit sleep stmt as elements would take sometime to load,
# but selenium will not check if below resultslist is empty or not. Therefore, implicit wait will not work
resultslist = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(resultslist))
assert len(resultslist) != 0

for result in resultslist:
     #Chain Locator i.e. starting the line with result. instead of driver. , therefore limiting the search only to elements list
     actuallist.append(result.find_element(By.XPATH, "h4").text)
     #result.find_element(By.XPATH, "div/button").click()
     result.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

print(actuallist)
assert actuallist == expectedlist

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.CLASS_NAME, "promoInfo"))
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo"))) #specified braces are so important and need to be exact
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

assert driver.find_element(By.CLASS_NAME, "promoInfo").text == 'Code applied ..!'

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
assert int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) == sum
#this stmt will fail...assert int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) > int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) > float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()


driver.close()