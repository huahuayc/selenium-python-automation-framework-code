import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from page.yatra_launch_page import Launchpage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        # launching browser and opening the travel website: conftest
        lp = Launchpage(self.driver)

        # provide the departure place
        lp.departfrom("New Delhi")

        # provide arrival place
        lp.goingto("New York")
        # To resolve sync issues

        #select the departure date
        lp.selectdate("12/12/2022")

        #Click on flight search button
        lp.clicksearch()

        # To handle dynamic scroll

        #select the filter 1 stop

        # Verify that the filtered result show flights having only 1 stop
        #allstops1 = lp.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        #print(len(allstops1))



# dauto = TestSearchAndVerifyFilter()
# dauto.test_search_flights()