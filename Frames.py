from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
#driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Test Comment")

# windowslist = driver.window_handles
# print(windowslist)
# driver.switch_to.window(windowslist[0])

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)

