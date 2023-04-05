from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver1.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
assert(driver.current_url == "https://rahulshettyacademy.com/")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
assert(driver.current_url == "https://rahulshettyacademy.com/")
driver.refresh()
driver.forward()
assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/")
driver.close()