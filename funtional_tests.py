from selenium import webdriver

#browser = webdriver.Firefox()
browser = webdriver.Chrome("./tools/mac_chromedriver")

browser.get("http://localhost:8000")

assert 'Django' in browser.title

