from selenium import  webdriver
import time
#For Firefox
"""profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
dr = webdriver.Firefox(firefox_profile=profile)
#dr = webdriver.Firefox()"""

#For Chrome
"""options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
dr = webdriver.Chrome(chrome_options=options)
dr.get("https://cacert.org/")
time.sleep(3)
"""
#For Internet Explorer

cap = webdriver.DesiredCapabilities.INTERNETEXPLORER
cap['acceptSslCerts'] = True
dr = webdriver.Ie(capabilities=cap)
dr.get("https://cacert.org/")
time.sleep(6)
dr.quit()