from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setUp():
    chrome_option = Options()   
    chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_option ,executable_path="C:\\Users\\hdthien\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = "https://register.codx.vn/Shopping?_=trial"
    driver.get(url)
    return driver

driver = setUp()

for i in range(1,9):
    checkbox = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[%s]/div/label" %i)
    checkbox.click()

driver.save_screenshot("Screen_Home.png")
btnNext = driver.find_element("xpath","//*[text()='Next']")
btnNext.click()
time.sleep(3)

name = datetime.now().strftime("%d%m%y%H%M")
mail = name + '@yopmail.com'
pw = "Hoilamgi123@@"

def register():
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
    driver.save_screenshot("Screen_LoginCODX.png")
    # 
    site_create = loginCODX.get_attribute("href")
    print(site_create)
    
    with open('data.txt', 'w') as f:
        f.writelines(site_create)    
        f.writelines("\n")
        f.writelines(mail)
        f.writelines("\n")
        f.writelines(pw)
        f.writelines("\n")
        f.close()
        
    driver.get(site_create)
    user = driver.find_element("xpath","//input[@placeholder='Nhập tài khoản hoặc email']")
    user.send_keys(mail)
    passw2 = driver.find_element("xpath","//input[@placeholder='Mật khẩu']")
    passw2.send_keys(pw)
    passw2.submit()
    time.sleep(5)
    driver.save_screenshot("Scree_SiteRegister.png")
  
def changePass():
    new_pass = pw + '@'
    time.sleep(3)
    avt = driver.find_element("xpath","/html/body/lib-layout-portal/div[3]/div/div/codx-header/div/div[3]/div/codx-user-inner/div/button/codx-img/div/div")
    avt.click()
    time.sleep(1)
    changePassLbl = driver.find_element("xpath","//span[@data-name='lblChangePass']")
    changePassLbl.click()
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID,"btn-signin")))
    driver.save_screenshot("Screen_ChangePass.png")
    # 
    user = driver.find_element("xpath","//input[@placeholder='Nhập tài khoản hoặc email']")
    user.send_keys(mail)
    old_pw = driver.find_element("xpath","//input[@placeholder='Mật khẩu cũ']")
    old_pw.send_keys(pw)
    new_pw = driver.find_element("xpath","//input[@placeholder='Mật khẩu mới']")
    new_pw.send_keys(new_pass)
    confirm_pw = driver.find_element("xpath","//input[@placeholder='Mật khẩu mới']")
    confirm_pw.send_keys(new_pass)
    
def main():
    register()
    time.sleep(2)
    print("Register Done !!")
    
if __name__ == "__main__":
    main()