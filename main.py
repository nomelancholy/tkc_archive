from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://naver.com/")

login_button = driver.find_element_by_css_selector(".link_login")

driver.get("https://dctribe.com/")

driver.get("https://hiphople.com/")

driver.get("http://www.todayhumor.co.kr/")

login_button.click()