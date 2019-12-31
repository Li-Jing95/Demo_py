from selenium import webdriver
from time import *
driver = webdriver.Chrome()
driver.get("http://oa.esafenet.com:8080")
sleep(5)

driver.add_cookie({'name':'ecology_JSessionId','value':'abcqMy-ckaf88aCtf--8w'})
driver.refresh()