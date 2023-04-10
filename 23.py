# testing - selenium, selenium is a test tool that mostly get used for web application
import time

from selenium import webdriver
from time import sleep
# binary in directory C:\Windows\System32, so can keep empty webdriver.Chrome(), otherwise need to add the executable_path location, for example("c:/temp/download")
driver = webdriver.Chrome()
#driver.get("https://github.com")
driver.get("file://C:/devops_expert/lesson4-testing/index.html")
# this we take from xpath - by enconding in html
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys("5")
driver.find_element(by="id", value="calculate").click()
expected = "2.00"
actual = driver.find_element(by="id", value="tip").text
assert expected != actual
#or
#if expected == actual:
#    print("tip calc is ok")
sleep(5)
driver.close()
#C:\devops_expert\lesson4-testing