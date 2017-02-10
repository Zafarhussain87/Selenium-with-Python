from selenium import webdriver
import time

dr = webdriver.Chrome()

dr.get("http://zafar:hussain@www.engprod-charter.net/")
time.sleep(5)
dr.quit()