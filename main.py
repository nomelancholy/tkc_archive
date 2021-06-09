import os
from selenium import webdriver
from dotenv import load_dotenv,find_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://naver.com/")
load_dotenv(find_dotenv())

NAVER_ID = os.environ.get("NAVER_ID")

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'link_login'))
    )
except:
    driver.quit()

login_button = driver.find_element_by_css_selector(".link_login")

login_button.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'id_area'))
    )
except:
    driver.quit()

input_field = driver.find_element_by_id('id')
pw_field = driver.find_element_by_id('pw_area')

input_field.click()
input_field.send_keys(NAVER_ID)


# driver.get("https://dctribe.com/")
#
# driver.get("https://hiphople.com/")
#
# driver.get("http://www.todayhumor.co.kr/")

