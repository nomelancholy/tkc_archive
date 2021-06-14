import os
import time
import pyperclip

from selenium import webdriver
from dotenv import load_dotenv,find_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
load_dotenv(find_dotenv())

def naver_process():
    driver.get("http://naver.com/")

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
    time.sleep(1.5)

    submit_button = driver.find_element_by_id("log.login")
    submit_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[3]/a'))
        )
    except:
        driver.quit()

    driver.get('https://blog.naver.com/starmekey/postwrite')

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'se-help-panel-close-button'))
        )
    except:
        driver.quit()

    time.sleep(2)

    popup_close_button = driver.find_element_by_class_name('se-help-panel-close-button')
    popup_close_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'SE-07f5820a-3947-4e98-97dd-cfce58671d43'))
        )
    except:
        driver.quit()

    # time.sleep(3)

    # driver.execute_script("document.getElementsById('SE-07f5820a-3947-4e98-97dd-cfce58671d43')[0].value=\'"+'테스트'+"\'")
    # title_field = driver.find_element_by_id('SE-07f5820a-3947-4e98-97dd-cfce58671d43')

    # title_field.send_keys('자동화 귀찮다')


def dct_process():
    driver.get("https://dctribe.com/")

    DCT_ID = os.environ.get("DCT_ID")
    DCT_PW = os.environ.get("DCT_PW")

def hiphople_process():
    driver.get("https://hiphople.com/")

    HIPHOPLE_ID = os.environ.get("HIPHOPLE_ID")
    HIPHOPLE_PW = os.environ.get("HIPHOPLE_PW")

def o_u_process():
    driver.get("http://www.todayhumor.co.kr/")

    O_U_ID = os.environ.get("O_U_ID")
    O_U_PW = os.environ.get("O_U_PW")


# naver_process()
dct_process()
# hiphople_process()
# o_u_process()


