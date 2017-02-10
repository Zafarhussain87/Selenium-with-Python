print("hello world")

from selenium import webdriver
driver = webdriver.Chrome("D:\\Selenium\\browsers\\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://www.facebook.com")
driver.maximize_window()
print(driver.title)
assert "Facebook" in driver.title
driver.get_screenshot_as_file("C:\\Users\\Zafar Hussain\\PycharmProjects\\Testing_Scripts\\screenshots\\homepage.png")
driver.implicitly_wait(10)
driver.find_element_by_id("email").send_keys("zafar@zafar.com")
driver.find_element_by_name("pass").send_keys("ghvhxax")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("C:\\Users\\Zafar Hussain\\PycharmProjects\\Testing_Scripts\\screenshots\\error.png") #if no specified path, it will save to project directory
driver.quit()



