from selenium import webdriver

import time
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.openFile", "application/octet-stream")
dr = webdriver.Firefox(profile)

dr.get("http://filehippo.com/download_free_pdf_reader/")
dr.find_element_by_xpath("//*[@id='program-header']/div[2]/a[1]").click()
time.sleep(5)
dr.quit()