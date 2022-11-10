import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    serv_obj = Service()
    driver = webdriver.Chrome(service=serv_obj)
    #wait = WebDriverWait(driver,10)
    url = "https://www.yatra.com/"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait
    # yield
    # driver.close()