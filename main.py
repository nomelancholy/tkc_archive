import os
import time
import pyperclip

from selenium import webdriver
from dotenv import load_dotenv,find_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def naver_process():
    driver.get("http://naver.com/")
    load_dotenv(find_dotenv())

    NAVER_ID = os.environ.get("NAVER_ID")
    NAVER_PW = os.environ.get("NAVER_PW")

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

    id_field = driver.find_element_by_id('id')
    pw_field = driver.find_element_by_id('pw')

    id_field.click()
    pyperclip.copy(NAVER_ID)
    id_field.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    pw_field.click()
    pyperclip.copy(NAVER_PW)
    pw_field.send_keys(Keys.CONTROL, 'v')
    time.sleep(2)

    submit_button = driver.find_element_by_id("log.login")
    submit_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[3]/a'))
        )
    except:
        driver.quit()

    driver.get('https://blog.naver.com/starmekey')


def dct_process():
    driver.get("https://dctribe.com/")

def hiphople_process():
    driver.get("https://hiphople.com/")

def o_u_process():
    driver.get("http://www.todayhumor.co.kr/")

naver_process()
# dct_process()
# hiphople_process()
# o_u_process()


