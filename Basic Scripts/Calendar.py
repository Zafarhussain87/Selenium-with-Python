from selenium import webdriver
import time
dr = webdriver.Firefox()

dr.get("http://redbus.in")
dr.find_element_by_xpath(".//label[@for='onward_cal']").click()
lis = dr.find_element_by_xpath("//*[@id='rb-calendar_onward_cal']/table[1]")
print(lis.get_attribute("innerText"))
dat = (lis.get_attribute("innerText"))
for d in dat:
    print(d)
if dat==31:
        dat.click()

dr.close()