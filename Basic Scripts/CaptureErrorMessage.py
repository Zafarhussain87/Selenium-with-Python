from selenium import webdriver
import time

dr = webdriver.Firefox()
dr.get("http://www.gmail.com")
exp_msg = "Please enter your email. "
dr.find_element_by_id("next").click()
time.sleep(3)
act_msg = dr.find_element_by_xpath("//*[@id='errormsg_0_Email']").get_attribute("innerHTML")

print("Original message is "+act_msg)
assert exp_msg in act_msg

dr.quit()


