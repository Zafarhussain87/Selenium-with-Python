from selenium import  webdriver

dr = webdriver.Firefox()

dr.get("http://seleniumpractise.blogspot.fi/2016/11/handle-bootstrap-model-dialog-in.html")
dr.find_element_by_xpath("//button[text()='Click here to Login']").click()
dr.find_element_by_xpath("//input[@type='text']").send_keys("zafar")
dr.find_element_by_xpath("//input[@type='password']").send_keys("fasfas")
dr.find_element_by_xpath("//input[@type='submit']").click()
print(dr.title)

dr.implicitly_wait(5)

dr.close()