from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

dr = webdriver.Firefox()

dr.get("http://seleniumpractise.blogspot.fi/2016/08/how-to-use-explicit-wait-in-selenium.html")

#elem = \
WebDriverWait(dr,5).until(ec.presence_of_element_located((By.XPATH, "//button[text()='Click me to start timer']"))).click()
#elem.click()

time.sleep(3)
