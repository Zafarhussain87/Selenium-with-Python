import logging
import time
from selenium import webdriver

logging.basicConfig(filename="Log File.log", level=logging.DEBUG)
dr = webdriver.Firefox()
logging.info("The Browser started. ")
dr.get("http://www.ksrtc.in/")
logging.info("Application launched")
dr.find_element_by_xpath("//*[@id='searchBtn']").click()
logging.info("Search button clicked")
print(dr.switch_to_alert().text)
logging.info("Printing mesage")
dr.switch_to_alert().accept()
logging.info("Alert is accepted")
time.sleep(3)
dr.quit()