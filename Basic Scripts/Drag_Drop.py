from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
import  time

dr = webdriver.Chrome()

dr.get("http://jqueryui.com/resources/demos/droppable/default.html")

src = dr.find_element_by_xpath("//*[@id='draggable']")
tar = dr.find_element_by_xpath("//*[@id='droppable']")

act = ActionChains(dr)
act.drag_and_drop(src, tar).perform()

time.sleep(3)

dr.quit()
