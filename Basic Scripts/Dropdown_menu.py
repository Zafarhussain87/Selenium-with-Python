from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
dr = webdriver.Firefox()
dr.get("http://www.facebok.com")

dr.find_element_by_xpath("//input[@id='u_0_1']").send_keys("zagxsas")

dr.find_element_by_xpath("//input[contains(@name,'last')]").send_keys("ahcajcadc")

dr.find_element_by_xpath("//input[@name='sex'][@value='2']").click()

select_month = Select(dr.find_element_by_xpath(".//*[@id='month']"))
select_month.select_by_index(5)

select_day = Select(dr.find_element_by_id("day"))
select_day.select_by_index(23)

select_year = Select(dr.find_element_by_id("year"))
select_year.select_by_value("2010")

dr.find_element_by_id("u_0_e").click()

dr.find_element_by_xpath("//a[@href='/pages/create/?ref_type=registration_form']").click()

time.sleep(3)
dr.back()