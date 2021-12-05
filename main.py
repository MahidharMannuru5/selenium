import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

Driver_path=Service('/path/chromedriver')
browser=webdriver.Chrome(service=Driver_path)
browser.get("https://lovecalcforu.000webhostapp.com/")
name=browser.find_element_by_id("name")
name.send_keys("Mahidhar")
crush=browser.find_element_by_id("crush")
crush.send_keys("Mannuru")
login=browser.find_element_by_name("sub")
login.click()
