from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
dr = webdriver.Chrome()

dr.get("http://seleniumpractise.blogspot.fi/2016/08/how-to-perform-mouse-hover-in-selenium.html")
time.sleep(3)
el = dr.find_element_by_xpath("//button[text()='Automation Tools']")
time.sleep(3)
Hover = ActionChains(dr).move_to_element(el)
Hover.perform()
lis = dr.find_elements_by_xpath("//div[@class='dropdown-content']//a")
time.sleep(3)

for l in lis:
    st = l.text
    print(st)
    if st=="TestNG":
        l.click()
        time.sleep(5)
dr.quit()