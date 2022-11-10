import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class Launchpage(BaseDriver):
    def __init__(self, driver):
        self.driver = driver
        #self.wait = wait

    def departfrom(self, departllocation):
        # depart_from = self.wait_until_element_to_be_clickable(By.XPATH,"//input[@id='BE_flight_origin_city']")
        # depart_from.click()
        # depart_from.send_keys(departllocation)
        # depart_from.send_keys(Keys.ENTER)
        depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys(departllocation)
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)

    def goingto(self,goingtolocation):
        going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")
        time.sleep(2)
        going_to.send_keys(Keys.ENTER)
        time.sleep(4)

    def selectdate(self, departuredate):
        origin = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)

        all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class != 'inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                time.sleep(4)
                break

    def clicksearch(self):
        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(4)







