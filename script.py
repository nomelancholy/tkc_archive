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

# chrome driver setup
driver = webdriver.Chrome(r"C:\webdriver\chromedriver.exe")
load_dotenv(find_dotenv())

# find text file
# text = open("G:\\T.K.C\\take knowledge's choice.txt", 'rt', encoding='UTF8')

# read text file and split based on \
# list = text.read().split('\\')

# Take Knowledge's Choice #1832. J. Rawls - Blue #2 (2001) \
FULL_TITLE = "Take Knowledge's Choice #1913. All Natural - Elements of Style (2001)"
split_title = FULL_TITLE.split('.', maxsplit=1)
# Take Knowledge's Choice #1832
INDEX_TITLE = split_title[0]
# J. Rawls - Blue #2 (2001)
TITLE = split_title[1].lstrip()

CONTENT = "All Natural의 2001년 작 \n Elements of Style입니다 \n \n 즐감하세요! \n \n 그간 올린 곡들은 블로그와 \n 네이버 카페 '랩잡'의 'Take Knowledge' 카테고리에서도 만나 보실 수 있습니다. \n  \n http://blog.naver.com/starmekey \n https://cafe.naver.com/rapsup"

split_content = CONTENT.split('\n')
HTML_CONTENT = ['<br />' if line == '' else "<p>"+line+"</p>" for line in split_content]

LINK_TYPE = 'audio'

YOUTUBE_LINK = 'https://youtu.be/h8rxXGoByy8'
IFRAME_LINK = '<iframe width="560" height="315" src="https://www.youtube.com/embed/'+YOUTUBE_LINK.split('/')[3]+'" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

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

    time.sleep(3)

    driver.execute_script("document.getElementsById('SE-07f5820a-3947-4e98-97dd-cfce58671d43')[0].value=\'"+'테스트'+"\'")
    title_field = driver.find_element_by_id('SE-07f5820a-3947-4e98-97dd-cfce58671d43')

    title_field.send_keys(FULL_TITLE)

    # driver.get('https://cafe.naver.com/rapsup')
    #
    # tk_link = driver.find_element_by_link_text('Take Knowledge')
    #
    # tk_link.click()

    driver.get('https://cafe.naver.com/ca-fe/cafes/14371899/menus/571/articles/write?boardType=L')

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'textarea_input'))
        )
    except:
        driver.quit()

    cafe_title_field = driver.find_element_by_class_name('textarea_input')
    cafe_title_field.click()
    cafe_title_field.send_keys(FULL_TITLE)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'se-text-paragraph'))
        )
    except:
        driver.quit()

    cafe_content_field = driver.find_element_by_class_name("se-text-paragraph")
    # cafe_content_field = driver.find_element_by_xpath("//div[@class='se-content']//following::span[@class='se-placeholder']")

    cafe_content_field.click()
    cafe_content_field.send_keys('test')


def dct_process():
    driver.get("https://dctribe.com/")

    DCT_ID = os.environ.get("DCT_ID")
    DCT_PW = os.environ.get("DCT_PW")

    # id_field = driver.find_element_by_id("user_id")
    id_field = driver.find_element(by=By.ID, value="user_id")
    id_field.send_keys(DCT_ID)

    # pw_field = driver.find_element_by_id("passwd")
    pw_field = driver.find_element(by=By.ID, value="passwd")
    pw_field.send_keys(DCT_PW)

    # login_button = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="login"]/form/div[3]/input')
    login_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'account'))
        )
    except:
        driver.quit()

    if LINK_TYPE == 'audio':
        driver.get("https://dctribe.com/0/zboard.php?id=audio")
    elif LINK_TYPE == 'video':
        driver.get("https://dctribe.com/0/zboard.php?id=video")

    # write_button = driver.find_element_by_xpath('//*[@id="bottom"]/div[2]/a')
    write_button = driver.find_element(by=By.XPATH, value='//*[@id="bottom"]/div[2]/a')
    write_button.click()

    # category_select = Select(driver.find_element_by_xpath('//*[@id="post"]/form/div[1]/select'))
    category_select = Select(driver.find_element(by=By.XPATH, value='//*[@id="post"]/form/div[1]/select'))
    category_select.select_by_visible_text("foreign")

    # title_field = driver.find_element_by_class_name('post_input')
    title_field = driver.find_element(by=By.CLASS_NAME, value='post_input')
    title_field.send_keys(FULL_TITLE)

    # iframe = driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
    iframe = driver.find_element(by=By.XPATH, value='//*[@id="cke_1_contents"]/iframe')
    driver.switch_to.frame(iframe)

    # editor = driver.find_element_by_xpath('/html/body')
    editor = driver.find_element(by=By.XPATH, value='/html/body')
    editor.send_keys(CONTENT)

    driver.switch_to.default_content()
    #
    # link_field = driver.find_element_by_xpath('//*[@id="post"]/form/div[8]/input')
    link_field = driver.find_element(by=By.XPATH, value='//*[@id="post"]/form/div[8]/input')
    link_field.send_keys(YOUTUBE_LINK)

    time.sleep(2)
    #
    upload_button = driver.find_element(by=By.XPATH, value='//*[@id="delete"]')
    upload_button.click()
    
def hiphople_process():
    driver.get("https://hiphople.com/")

    HIPHOPLE_ID = os.environ.get("HIPHOPLE_ID")
    HIPHOPLE_PW = os.environ.get("HIPHOPLE_PW")

    # popup_load_btn = driver.find_element_by_class_name('tg_btn')
    popup_load_btn = driver.find_element(by=By.CLASS_NAME, value='tg_btn')

    popup_load_btn.click()

    # id_field = driver.find_element_by_id("uid")
    id_field = driver.find_element(by=By.ID, value="uid")
    id_field.send_keys(HIPHOPLE_ID)

    # pw_field = driver.find_element_by_id("upw")
    pw_field = driver.find_element(by=By.ID, value="upw")
    pw_field.send_keys(HIPHOPLE_PW)

    # login_btn = driver.find_element_by_class_name('login_btn')
    login_btn = driver.find_element(by=By.CLASS_NAME, value='login_btn')
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

    # write_btn = driver.find_element_by_xpath("//*[@id=\"aplosboard\"]/div[4]/div[2]/a[2]")
    write_btn = driver.find_element(by=By.XPATH, value="//*[@id=\"aplosboard\"]/div[4]/div[2]/a[2]")
    write_btn.click()

    # category_select = Select(driver.find_element_by_id("category"))
    category_select = Select(driver.find_element(by=By.ID, value="category"))
    category_select.select_by_visible_text("음악")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"gap\"]/div/div/form/div[2]/div[2]/input"))
        )
    except:
        driver.quit()

    # title_field = driver.find_element_by_xpath("//*[@id=\"gap\"]/div/div/form/div[2]/div[2]/input")
    title_field = driver.find_element(by=By.XPATH, value="//*[@id=\"gap\"]/div/div/form/div[2]/div[2]/input")
    title_field.send_keys(FULL_TITLE)

    # html_code_button = driver.find_element_by_id('cke_40')
    html_code_button = driver.find_element(by=By.ID, value='cke_40')
    html_code_button.click()

    # html_editor = driver.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea')
    html_editor = driver.find_element(by=By.XPATH, value='//*[@id="cke_1_contents"]/textarea')
    html_editor.send_keys(IFRAME_LINK)

    # disable_code = driver.find_element_by_xpath('//*[@id="cke_40"]')
    disable_code = driver.find_element(by=By.XPATH, value='//*[@id="cke_40"]')
    disable_code.click()

    # iframe = driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
    iframe = driver.find_element(by=By.XPATH, value='//*[@id="cke_1_contents"]/iframe')
    driver.switch_to.frame(iframe)

    # editor = driver.find_element_by_xpath('/html/body/p')
    editor = driver.find_element(by=By.XPATH, value='/html/body/p')
    editor.send_keys('\n\n')
    editor.send_keys(CONTENT)

    driver.switch_to.default_content()
    # reg_btn = driver.find_element_by_id('cmd_reg')
    reg_btn = driver.find_element(by=By.ID, value='cmd_reg')
    reg_btn.click()

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

    # id_field = driver.find_element_by_xpath('//*[@id="id"]')
    id_field = driver.find_element(by=By.XPATH, value='//*[@id="id"]')
    id_field.send_keys(O_U_ID)

    # pw_field = driver.find_element_by_id("passwd")
    pw_field = driver.find_element(by=By.ID, value="passwd")
    pw_field.send_keys(O_U_PW)

    # login_button = driver.find_element_by_class_name("login_btn")
    login_button = driver.find_element(by=By.CLASS_NAME, value="login_btn")
    login_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_user_menu"]/span'))
        )
    except:
        driver.quit()

    driver.get("http://www.todayhumor.co.kr/board/write.php?table=music")

    # title_field = driver.find_element_by_id('subject')
    title_field = driver.find_element(by=By.ID, value='subject')
    title_field.send_keys(INDEX_TITLE)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cheditor-tab-code-off'))
        )
    except:
        driver.quit()

    # frame_change_to_html_button = driver.find_element_by_class_name('cheditor-tab-code-off')
    frame_change_to_html_button = driver.find_element(by=By.CLASS_NAME, value='cheditor-tab-code-off')
    frame_change_to_html_button.click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cheditor-editarea-text-content'))
        )
    except:
        driver.quit()

    # html_area = driver.find_element_by_class_name('cheditor-editarea-text-content')
    html_area = driver.find_element(by=By.CLASS_NAME, value='cheditor-editarea-text-content')
    html_area.send_keys(IFRAME_LINK)
    html_area.send_keys(HTML_CONTENT)

    # frame_change_to_editor_button = driver.find_element_by_class_name('cheditor-tab-rich-off')
    frame_change_to_editor_button = driver.find_element(by=By.CLASS_NAME, value='cheditor-tab-rich-off')
    frame_change_to_editor_button.click()

    # submit_button = driver.find_element_by_xpath('//*[@id="write_form"]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/div/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="write_form"]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/div/input')
    submit_button.click()

# naver_process()
dct_process()
# hiphople_process()
# o_u_process()

