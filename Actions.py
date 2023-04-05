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
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.click_and_hold()
# action.double_click(driver.find_element(By.ID, ""))
# action.drag_and_drop()
action.scroll_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
#action.send_keys(Keys.ESCAPE).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
