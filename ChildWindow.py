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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowslist = driver.window_handles
print(windowslist)
driver.switch_to.window(windowslist[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() #--> if you want to close only child window
driver.switch_to.window(windowslist[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
#driver.quit() # --> if you want to close both windows

time.sleep(3)

#Assignment
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.PARTIAL_LINK_TEXT, "Free Access").click()
windowslist2 = driver.window_handles
print(windowslist)
driver.switch_to.window(windowslist2[1])
uname = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(uname)
driver.close()
driver.switch_to.window(windowslist2[0])
driver.find_element(By.ID, "username").send_keys(uname)
driver.find_element(By.ID, "password").send_keys("abcdef")
driver.find_element(By.NAME, "terms").click()
driver.find_element(By.NAME, "signin").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
print(driver.find_element(By.CLASS_NAME, "alert-danger").text)


