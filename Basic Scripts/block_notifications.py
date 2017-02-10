from selenium import webdriver



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
dr = webdriver.Chrome(chrome_options=chrome_options)
dr.get("http://www.facebook.com")

dr.close()
