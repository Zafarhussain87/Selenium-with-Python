from selenium import webdriver

import time

dr = webdriver.Firefox()
dr.get("http://seleniumpractise.blogspot.fi/2016/09/how-to-work-with-disable-textbox-or.html")

dr.execute_script("document.getElementById('pass').value='zafar hussain'")

time.sleep(3)