from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") # headless mode for chrome
chrome_options.add_experimental_option('detach', True) #stops automatic closure of the browser, new feature added in latest chrome webdriver
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized") #starts window in maximized mode

#ua_argument = 'User-Agent="' + GetUserAgent() + '"'
#chrome_options.add_argument(ua_argument)

service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#driver.implicitly_wait(3)
#driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
#driver.quit()
