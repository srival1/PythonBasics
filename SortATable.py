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


service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

itemsperpage_dropdown = Select(driver.find_element(By.ID, 'page-menu'))
itemsperpage_dropdown.select_by_visible_text("20")
driver.find_element(By.XPATH, "//th/span[text()='Veg/fruit name']").click()

vegfruit_elementslist = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
#print(len(sortednameslist))
vegfruit_nameslist = []

for name in vegfruit_elementslist:
    vegfruit_nameslist.append(name.text)

originalnameslist = vegfruit_nameslist.copy()
vegfruit_nameslist.sort()

assert originalnameslist == vegfruit_nameslist
print(originalnameslist)
print(vegfruit_nameslist)


#custom function to check if a list is sorted
def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

sample_list = [5, 2, 3, 4, 1]
sample_list.sort()

assert is_sorted(vegfruit_nameslist) == True
assert is_sorted(sample_list) == True

driver.quit()
