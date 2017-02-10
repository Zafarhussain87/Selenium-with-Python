from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Firefox()

dr.get("https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en")

dr.find_element_by_xpath(".//*[@id='GmailAddress']").click()
act = ActionChains(dr)
ele = dr.find_elements_by_xpath("html/body/div[3]")
hov = act.move_to_element(ele)
hov.perform()
st = ele.text
print(st)
