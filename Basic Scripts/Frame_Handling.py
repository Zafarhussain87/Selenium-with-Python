from selenium import webdriver
import time


dr = webdriver.Firefox()
dr.get("file:///C:/Users/Zafar%20Hussain/Desktop/frames.html")

dr.switch_to.frame("w3c")
dr.find_element_by_xpath("//a[@title='Search W3Schools']").click()
time.sleep(3)
dr.find_element_by_name("search").click()
dr.find_element_by_name("search").send_keys("css")
time.sleep(2)
dr.find_element_by_xpath("//*[@title='search'][@type='image']").click()
dr.switch_to.default_content()
time.sleep(3)
tot = len((dr.find_elements_by_tag_name("iframe")))
print("total frames are "+str(tot))
dr.switch_to.parent_frame()
el = dr.find_element_by_xpath("//iframe[@title='selenium_news']")
dr.switch_to.frame(el)
dr.find_element_by_xpath("//a[@title='Selenium Projects']").click()
time.sleep(3)
dr.quit()