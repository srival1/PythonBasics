from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, XPath, CssSelector, ClassName, Name, LinkText, TagName

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("test name")
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("testpswd")
driver.find_element(By.CLASS_NAME, "form-check-input").click()

#XPATH = //tagname[@attribute='value']
#CssSelector = tagname[attribute='value'] or .ClassName or TagName.ClassName

driver.find_element(By.CSS_SELECTOR, "input.ng-pristine").clear()

#Static Dropdown - with fixed set of options to choose from
GenderDropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

#GenderDropdown.select_by_value("Female") --> Will Not Work as there's no value attribute for these options, useful when declared in html
GenderDropdown.select_by_visible_text("Female")
GenderDropdown.select_by_index(0)

driver.find_element(By.XPATH, "//input[@value='Submit']").click()
#driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
#driver.find_element(By.XPATH, "//input[@type='submit']").click()

#message = driver.find_element(By.CLASS_NAME, "alert-success").text
#message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
message = driver.find_element(By.CSS_SELECTOR, "div.alert-success").text
print(message)
#assert(message.__contains__("Success"))
#assert("Success" in message)
assert "Success" in message

#driver.close()

