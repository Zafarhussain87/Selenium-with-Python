from selenium import webdriver
dr = webdriver.Firefox()
import time
dr.get("http://www.tinyupload.com/")

elem = dr.find_element_by_xpath(".//*[@name='uploaded_file']")
elem.send_keys("D:\\Selenium\\fileupload.html")
time.sleep(3)

dr.quit()