import os
import time
import pyperclip

from selenium import webdriver
from dotenv import load_dotenv,find_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

    popup_load_btn = driver.find_element_by_class_name('tg_btn')
    popup_load_btn.click()

    id_field = driver.find_element_by_id("uid")
    id_field.send_keys(HIPHOPLE_ID)

    pw_field = driver.find_element_by_id("upw")
    pw_field.send_keys(HIPHOPLE_PW)

    login_btn = driver.find_element_by_class_name('login_btn')
    login_btn.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'LOGOUT'))
        )
    except:
        driver.quit()

    driver.get("https://hiphople.com/fboard")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"aplosboard\"]/div[4]/div[2]/a[2]"))
        )
    except:
        driver.quit()

    write_btn = driver.find_element_by_xpath("//*[@id=\"aplosboard\"]/div[4]/div[2]/a[2]")

    write_btn.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "cmd_reg"))
        )
    except:
        driver.quit()

    category_select = Select(driver.find_element_by_id("category"))
    category_select.select_by_visible_text("음악")

    title_field = driver.find_element_by_xpath("//*[@id=\"gap\"]/div/div/form/div[2]/div[2]/input")
    title_field.send_keys("제목 테스트")

    body_field = driver.find_element_by_xpath("/html/body/p")
    body_field.send_keys("안될 거 같은데")

def o_u_process():
    driver.get("http://www.todayhumor.co.kr/")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id"]'))
        )
    except:
        driver.quit()

    O_U_ID = os.environ.get("O_U_ID")
    O_U_PW = os.environ.get("O_U_PW")

    id_field = driver.find_element_by_xpath('//*[@id="id"]')
    id_field.send_keys(O_U_ID)

    pw_field = driver.find_element_by_id("passwd")
    pw_field.send_keys(O_U_PW)

    login_button = driver.find_element_by_class_name("login_btn")
    login_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_user_menu"]/span'))
        )
    except:
        driver.quit()

    driver.get("http://www.todayhumor.co.kr/board/write.php?table=music")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'subject'))
        )
    except:
        driver.quit()

    title_field = driver.find_element_by_id('subject')
    title_field.send_keys("제목 테스트")

# naver_process()
# dct_process()
# hiphople_process()
o_u_process()


