from selenium import  webdriver

import  time
dr = webdriver.Firefox()

dr.get("http://www.facebook.com")

el1 = dr.find_elements_by_css_selector("input[name='sex'][type='radio']")
for i in el1:
    st = i.get_attribute("value")
    print(st)
    if st=="2":
        print("its equal")
        i.click()

time.sleep(6)
dr.quit()