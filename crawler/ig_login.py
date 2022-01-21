from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.instagram.com/'

# ------ 前往該網址 ------
browser.get(url)

# ------ 填入帳號與密碼 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

# ------ 網頁元素定位 ------
# username_input = browser.find_elements_by_name('username')[0]
# password_input = browser.find_elements_by_name('password')[0]
username_input = browser.find_elements_by_name('username')[0]
password_input = browser.find_elements_by_name('password')[0]
print("inputing username and password...")

# ------ 輸入帳號密碼 ------
username_input.send_keys("leonard_nft_info")
password_input.send_keys("Xx189412")

# ------ 登入 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
# ------ 網頁元素定位 ------
login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
# ------ 點擊登入鍵 ------
login_click.click()

time.sleep(2)

# ------ 不儲存登入資料 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
# ------網頁元素定位 ------
store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
# ------ 點擊不儲存鍵 ------
store_click.click()

time.sleep(5)


# ------ 不開啟通知 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')))

# ------ 網頁元素定位 ------
notification_click = browser.find_elements_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')[0]

# ------ 點擊不開啟通知 ------
notification_click.click()
print("Log in!")