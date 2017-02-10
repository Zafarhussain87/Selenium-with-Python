from selenium import webdriver
import time
dr = webdriver.Chrome()

dr.get("https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default")
dr.implicitly_wait(5)
parent = dr.window_handles[0]
print(parent)
print ("Parent window is "+dr.title)

dr.find_element_by_xpath("//a[text()='Learn more']").click()
child = dr.window_handles[1]
dr.switch_to.window(child)
print(child)
print("Child window is "+dr.title)
time.sleep(3)
dr.switch_to.window(parent)

dr.quit()