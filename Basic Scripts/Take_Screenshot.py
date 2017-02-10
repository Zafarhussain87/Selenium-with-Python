from selenium import webdriver
import time
dr =webdriver.Firefox()
dr.get("http://www.facebook.com")
dr.save_screenshot("D://Selenium//python.png")
time.sleep(3)
dr.quit()