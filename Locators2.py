from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")

#ID, XPath, CssSelector, ClassName, Name, LinkText, TagName
#XPATH = //tagname[@attribute='value']
#CssSelector = tagname[attribute='value'] or .ClassName or TagName.ClassName

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("123456789")
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
message = driver.find_element(By.ID, "toast-container").text
assert "Password" in message

#driver.close()
