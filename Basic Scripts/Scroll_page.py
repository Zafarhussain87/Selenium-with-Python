from selenium import webdriver
dr = webdriver.Firefox()

import time

dr.get("http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html")
time.sleep(2)

dr.execute_script("scroll(0,700)")
time.sleep(2)

ele = dr.find_element_by_xpath(".//*[@id='mCSB_3_container']/p[4]")
dr.execute_script("arguments[0].scrollIntoView(true);", ele)

time.sleep(3)

dr.quit()