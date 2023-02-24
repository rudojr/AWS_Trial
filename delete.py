from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import shutil

class readFile():
    def __init__(self) -> None:
        with open("data.txt") as f:
            lines = f.read() 
            self.email = lines.split('\n',2)[1]
            self.password = lines.split('\n',3)[2]

def getPath(folderName):
    currentPath = os.path.dirname(os.path.realpath(__file__))
    directory = folderName
    check_path = os.path.join(currentPath, directory)
    isDir = os.path.isdir(check_path)
    if (isDir == True):
        shutil.rmtree(check_path)
        os.makedirs(check_path)
        return check_path  
    else:
        os.makedirs(check_path)
        return check_path 

def readData():
    return readFile()
data = readData()

def setUp():
    chrome_option = Options()   
    chrome_option.add_experimental_option('excludeSwitches', ['disable-logging'])
    # chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_option ,executable_path="C:\\Users\\hdthien\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://172.16.7.34:8111/Shopping')
    return driver

driver = setUp()

def login():
    folderPath = getPath('login')
    driver.find_element("xpath","/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div").click()
    lblSignin = driver.find_element("xpath","//span[text()='Sign in']")
    lblSignin.click()
    email = driver.find_element("id","Email")
    email.send_keys(data.email)
    password = driver.find_element("id","Password")
    password.send_keys(data.password)
    btnDangNhap = driver.find_element("id","btn-signin")
    btnDangNhap.click()
    driver.save_screenshot("%s/tenant_shopping.png" %folderPath)
    
def getAllTenant():
    time.sleep(1)
    list_tenant = driver.find_elements('xpath','//a[@type="button"]')
    for tenant in list_tenant:
        print(tenant.get_attribute('href'))
        
   
def main():
    login()
    getAllTenant()
if __name__ == '__main__':
    main()