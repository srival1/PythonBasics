from selenium import webdriver
from selenium.webdriver.edge.service import Service
#
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
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