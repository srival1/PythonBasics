import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option('detach', True)
service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#ID, XPath, CssSelector, ClassName, Name, LinkText, TagName
#XPATH = //tagname[@attribute='value']
#CssSelector = tagname[attribute='value'] or .ClassName or TagName.ClassName

driver.find_element(By.ID, "autosuggest").send_keys("au")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#print(len(countries))
#print(countries) # will display elements info like Session ID & Element ID, rather than Element Value

if countries[0].text == 'Australia':
    #countries[0].click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class='ui-menu-item'] a"))))
else:
    for country in countries:
        if country.text == 'Australia':
            country.click()
            break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
#print(driver.find_element(By.ID, "autosuggest").text) .text feature will not work as the value do not exist when page loaded

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == 'Australia'

driver.close()
