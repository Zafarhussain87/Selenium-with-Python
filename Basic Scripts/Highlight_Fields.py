from selenium import webdriver
import time
dr = webdriver.Firefox()
dr.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")
el = dr.find_element_by_xpath("//*[@id='Email']")

dr.execute_script("arguments[0].setAttribute('style','background: red; border: 2px solid yellow;');" , el)
time.sleep(3)
dr.quit()