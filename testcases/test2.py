import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
url = "https://www.yatra.com/"
driver.get(url)
#driver.maximize_window()
depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
depart_from.click()
time.sleep(2)
depart_from.send_keys("New Delhi")  #"New Delhi"
time.sleep(2)
depart_from.send_keys(Keys.ENTER)
time.sleep(4)

going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
going_to.click()
time.sleep(2)
going_to.send_keys("New York")
time.sleep(2)
going_to.send_keys(Keys.ENTER)
time.sleep(4)
# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")).click()
origin = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
origin.click()
time.sleep(4)

all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class != 'inActiveTD']")
for date in all_dates:
    if date.get_attribute("data-date") == "12/12/2022":
        date.click()
        time.sleep(4)
        break



