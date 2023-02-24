from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

def setUp():
    chrome_option = Options()   
    chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_option ,executable_path="C:\\Users\\hdthien\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = "http://172.16.7.34:8000/2102230849/auth/login"
    driver.get(url)
    return driver

driver = setUp()

def login():
    time.sleep(1)
    user = driver.find_element("xpath","//input[@field='email']")
    user.send_keys('2102230849@yopmail.com')
    pw = driver.find_element("xpath","//input[@type='password']")
    pw.send_keys('Hoilamgi123@@',Keys.ENTER)
    time.sleep(2) 

def invite_user():
    menu = driver.find_element("xpath","/html/body/lib-layout-portal/div[3]/div/div/codx-header/div/div[3]/div/erm-quick-links-inner/div")
    menu.click()
    quanTriHeThong = driver.find_element("xpath","/html/body/lib-layout-portal/div[3]/div/div/codx-header/div/div[3]/div/erm-quick-links-inner/div/div/div/div[2]/a")
    quanTriHeThong.click()
    btnAdd = driver.find_element("xpath","//span[@data-name='btnAdd']")
    btnAdd.click()
    user_name = driver.find_element("xpath","//input[@placeholder='Nhập tên người dùng...']")
    user_name.send_keys("Hoang DUc Thien")
    driver.find_element("xpath","/html/body/lib-nosubaside/div[1]/div/aside/lib-add-user/codx-layout-add/codx-form/div/div[2]/div[2]/div/div/div[1]/div[4]/codx-input/codx-combobox/ejs-combobox/span/span").click()
    vungDuLieu = driver.find_element("xpath","//div[@title='Guest']")
    vungDuLieu.click()
    Email = driver.find_element("xpath","//input[@placeholder='Nhập email...']")
    Email.send_keys("admin_123@yopmail.com")
    btnSave = driver.find_element("xpath","//span[@data-name='Save']")
    btnSave.click()
    time.sleep(5)

def main():
    login()
    time.sleep(2)
    invite_user()

if __name__ == '__main__':
    main()