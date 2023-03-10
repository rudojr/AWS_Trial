from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
import time
import os
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def setUp():
    chrome_option = Options()   
    chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_option ,executable_path="C:\\Users\\hdthien\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = "http://172.16.7.34:8111/Shopping/"
    driver.get(url)
    return driver

driver = setUp()

for i in range(1,9):
    checkbox = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[%s]/div/label" %i)
    checkbox.click()

btnNext = driver.find_element("xpath","//*[text()='Next']")
btnNext.click()
time.sleep(2)

name = datetime.now().strftime("%d%m%y%H%M")
mail = name + '@yopmail.com'
pw = "Hoilamgi123@@"
new_pass = pw + '@'

def register():
    folderPath = getPath('8111')
    hoTen = driver.find_element("id","Fullname")
    hoTen.send_keys(name)
    # 
    email = driver.find_element("id","Email")
    email.send_keys(mail)
    # 
    passw = driver.find_element("id","Password")
    passw.send_keys(pw)
    # 
    confirm_passw = driver.find_element("id","ConfirmPassword")
    confirm_passw.send_keys(pw)
    # 
    companyName = driver.find_element("id","CompanyName")
    companyName.send_keys(name)
    # 
    companyPhone = driver.find_element("id","CompanyPhone")
    companyPhone.send_keys(name)
    # 
    companyWeb = driver.find_element("id","TenantID")
    companyWeb.send_keys(name)
    # 
    companySize = Select(driver.find_element("id","CompanySize"))
    companySize.select_by_value("2")
    # 
    companyTarget = Select(driver.find_element("id","CompanyTarget"))
    companyTarget.select_by_value("1")
    # 
    agreeTerms = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div/div[7]/div/label[2]/span")
    agreeTerms.click()
    # 
    btnDangKy = driver.find_element("xpath","//button[@type='submit']")
    time.sleep(3)
    btnDangKy.click()
    # 
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='LogIn CoDX']")))
    loginCODX = driver.find_element(By.XPATH, "//a[text()='LogIn CoDX']")
    driver.save_screenshot("%s/register.png" %folderPath)
    # 
    site_create = loginCODX.get_attribute("href")
        
    with open('%s/data.txt' %folderPath, 'w') as f:
        f.writelines(site_create)    
        f.writelines("\n")
        f.writelines(mail)
        f.writelines("\n")
        f.writelines(pw)
        f.writelines("\n")
        f.close()
        
    driver.get(site_create)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-auth/app-login/codx-login/div/div/div/div/div/div[1]/div/div[1]/div[2]/form/div[4]/button")))
    user = driver.find_element("xpath","//input[@placeholder='Nh???p t??i kho???n ho???c email']")
    user.send_keys(mail)
    passw2 = driver.find_element("xpath","//input[@placeholder='M???t kh???u']")
    passw2.send_keys(pw)
    btnDangNhap = driver.find_element("xpath","/html/body/app-auth/app-login/codx-login/div/div/div/div/div/div[1]/div/div[1]/div[2]/form/div[4]/button")
    btnDangNhap.click()
    time.sleep(2)
    driver.save_screenshot("%s/home page.png" %folderPath)
  
def register_2():
    
    folderPath = getPath('8111')
    
    # btnNext1 = driver.find_element("xpath","    ")
    # btnNext1.click()
    # 
    hoTen = driver.find_element("id","Fullname")
    hoTen.send_keys(name)
    # 
    email = driver.find_element("id","Email")
    email.send_keys(mail)
    # 
    passw = driver.find_element("id","Password")
    passw.send_keys(pw)
    # 
    confirm_passw = driver.find_element("id","ConfirmPassword")
    confirm_passw.send_keys(pw)
    # 
    companyName = driver.find_element("id","CompanyName")
    companyName.send_keys("CTY Thien")
    # 
    companyPhone = driver.find_element("id","CompanyPhone")
    companyPhone.send_keys(name)
    # 
    companyWeb = driver.find_element("id","TenantID")
    companyWeb.send_keys(name)
    # 
    companySize = Select(driver.find_element("id","CompanySize"))
    companySize.select_by_value("2")
    # 
    companyTarget = Select(driver.find_element("id","CompanyTarget"))
    companyTarget.select_by_value("1")
    # 
    agreeTerms = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div/div[7]/div/label[2]/span")
    agreeTerms.click()
    # 
    btnDangKy = driver.find_element("xpath","//button[@type='submit']")
    time.sleep(3)
    btnDangKy.click()
    # 
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='LogIn CoDX']")))
    loginCODX = driver.find_element(By.XPATH, "//a[text()='LogIn CoDX']")
    driver.save_screenshot("%s/register.png" %folderPath)
    # 
    site_create = loginCODX.get_attribute("href")
        
    with open('%s/data.txt' %folderPath, 'w') as f:
        f.writelines(site_create)    
        f.writelines("\n")
        f.writelines(mail)
        f.writelines("\n")
        f.writelines(pw)
        f.writelines("\n")
        f.close()
        
    driver.get(site_create)
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-auth/app-login/codx-login/div/div/div/div/div/div[1]/div/div[1]/div[2]/form/div[4]/button")))
    user = driver.find_element("xpath","//input[@placeholder='Nh???p t??i kho???n ho???c email']")
    user.send_keys(mail)
    passw2 = driver.find_element("xpath","//input[@placeholder='M???t kh???u']")
    passw2.send_keys(pw)
    btnDangNhap = driver.find_element("xpath","/html/body/app-auth/app-login/codx-login/div/div/div/div/div/div[1]/div/div[1]/div[2]/form/div[4]/button")
    btnDangNhap.click()
    time.sleep(2)
    driver.save_screenshot("%s/home page.png" %folderPath)
    

def changePass():
    avt = driver.find_element("xpath","/html/body/lib-layout-portal/div[3]/div/div/codx-header/div/div[3]/div/codx-user-inner/div/button/codx-img/div/div")
    avt.click()
    time.sleep(1)
    changePassLbl = driver.find_element("xpath","//span[@data-name='lblChangePass']")
    changePassLbl.click()
    time.sleep(1)
    # 
    user = driver.find_element("xpath","//input[@placeholder='Nh???p t??i kho???n ho???c email']")
    user.send_keys(mail)
    old_pw = driver.find_element("xpath","//input[@placeholder='M???t kh???u c??']")
    old_pw.send_keys(pw)
    new_pw = driver.find_element("xpath","//input[@placeholder='M???t kh???u m???i']")
    new_pw.send_keys(new_pass)
    confirm_pw = driver.find_element("xpath","//input[@placeholder='X??c nh???n m???t kh???u']")
    confirm_pw.send_keys(new_pass)
    driver.save_screenshot("Change pass.png")
    btnDangNhap = driver.find_element("id","btn-signin")
    btnDangNhap.click()
    time.sleep(1)
    driver.close()

def login_after_change_pass():
    chrome_option = Options()   
    chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_option ,executable_path="C:\\Users\\hdthien\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 
    with open("data.txt") as f:
        lines = f.read() 
        url = lines.split('\n', 1)[0]
    driver.get(url)
    # 
    user = driver.find_element("xpath","//input[@placeholder='Nh???p t??i kho???n ho???c email']")
    user.send_keys(mail)
    passw2 = driver.find_element("xpath","//input[@placeholder='M???t kh???u']")
    passw2.send_keys(new_pass)
    btnDangNhap = driver.find_element("xpath","/html/body/app-auth/app-login/codx-login/div/div/div/div/div/div[1]/div/div[1]/div[2]/form/div[4]/button")
    btnDangNhap.click()
    time.sleep(3)
    driver.save_screenshot("After Change pass.png")
       
def create_sdtc():
    driver.findElement(By.xpath("/html/body/lib-layout-portal/div[3]/div/div/codx-header/div/div[3]/div/erm-quick-links-inner/div/button")).click()
    driver.findElement(By.xpath("//span[text()='Qu???n tr??? nh??n s???']")).click()
    time.sleep(2)
    driver.findElement(By.xpath("//span[@class='menu-title' and text()='S?? ????? t??? ch???c']")).click()
    time.sleep(2)       

def main():
    register()
    time.sleep(2)
    # changePass()
    # login_after_change_pass()
    
if __name__ == "__main__":
    main()