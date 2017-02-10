from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time
dr = webdriver.Chrome()
dr.get("https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com")
act = ActionChains(dr)
act.move_to_element(dr.find_element_by_id("persistent")).click().perform()
time.sleep(3)
dr.quit()


