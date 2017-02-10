from selenium import webdriver
import time
dr = webdriver.Firefox()

dr.get("http://www.ksrtc.in/")
dr.find_element_by_xpath("//*[@id='searchBtn']").click()
print(dr.switch_to.alert.text)
time.sleep(3)
dr.switch_to.alert.accept()
time.sleep(3)
dr.quit()
