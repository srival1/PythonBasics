from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless") # headless mode for chrome
chrome_options.add_experimental_option('detach', True)
#chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("--start-maximized")

service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
# driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Sho").click()

#products_list = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
products_list = driver.find_elements(By.CSS_SELECTOR, ".card")

#//div[@class='card h-100']//h4/a
"""
#Below code is only for single product
for product in products_list:
    #if product.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
    if product.find_element(By.CSS_SELECTOR, "h4 a").text == "Blackberry":
        product.find_element(By.CSS_SELECTOR, "button").click()
"""
#Below code is for list of products
prod_list = ['Samsung Note 8', 'Blackberry']
for product in products_list:
    if product.find_element(By.CSS_SELECTOR, "h4 a").text in prod_list:
        product.find_element(By.CSS_SELECTOR, "button").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

driver.find_element(By.ID, "country").send_keys("in")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
#driver.find_element(By.CSS_SELECTOR, "#checkbox2").click() #this is not working for some reason, hence used below javascript executor stmt
driver.execute_script("document.getElementById('checkbox2').click()")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()

message = driver.find_element(By.CLASS_NAME, "alert").text
assert "Success! Thank you!" in message

assert driver.find_element(By.CLASS_NAME, "alert").text.__contains__("Success! Thank you!")

driver.quit()