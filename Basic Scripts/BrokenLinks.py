from selenium import webdriver

import requests



dr = webdriver.Firefox()
dr.get("http://www.facebook.com")
li =  dr.find_elements_by_tag_name("a")
for l in li:
    st = (l.get_attribute("href"))
    r = requests.head(st)
    print(st)
    if r.status_code==200:
        print("System is ok")
    else:
        print("its broken")

dr.close()
