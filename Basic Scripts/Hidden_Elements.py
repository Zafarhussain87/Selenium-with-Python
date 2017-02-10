from selenium import webdriver
import time
dr = webdriver.Firefox()

dr.get("http://seleniumpractise.blogspot.fi/2016/08/how-to-automate-radio-button-in.html")
element1 = dr.find_elements_by_xpath("//*[@id='male']")[1]
element1.click()
time.sleep(3)
dr.quit()
