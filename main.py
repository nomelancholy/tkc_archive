from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://naver.com/")

login_button = driver.find_element_by_css_selector(".link_login")

login_button.click()