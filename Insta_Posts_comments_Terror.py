import os
from sys import exec_prefix
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
import requests

# Complete these 2 fields ==================
USERNAME = 'whitehole00.xyz'
PASSWORD = 'jcm@040502'
# ==========================================

TIMEOUT = 10000000000


def scrape():
    usr = input('[Required] - Whose followers do you want to scrape: ')

    

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('window-size=1920x1080') 
   # options.add_argument('--start-fullscreen')
    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    

    bot.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    print("[Info] - Logging in...")

    user_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(USERNAME)

    time.sleep(0.1)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(5)
    print("login finish")

    bot.get('https://www.instagram.com/{}/'.format(usr))

    time.sleep(100000)
 #/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a/div/div[2]
    count = 14
    q = input("제일 최근에 올렸던 순서대로 1,2,3,4 입니다. (제일마지막에 올린게시물이 1번 예전에 올린걸수록 뒤로 갑니다.) ")
    
    try:
        WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div/div/div/div[{q}]/a/div'))).click()
    except Exception as e:
        print("없는 게시물 입니다.")    


if __name__ == '__main__':
    scrape()
#/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div/div/div/div[1]/a/div/div[2]
#/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div/div/div/div[2]/a/div/div[2]

#/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div/div/div/div[2]/a/div/div[1]

#/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div/div/div/div[1]/a