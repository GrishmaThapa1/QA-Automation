from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#lauch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open a login page
driver.get("http://localhost/complaint_management/login.php")
#maximize window
driver.maximize_window()
#Enter username
driver.find_element(By.ID,"username_or_email").send_keys("grishma@gmail.com")
#Enter password
driver.find_element(By.ID,"password").send_keys("ask@grishma")
#click on login
driver.find_element(By.CLASS_NAME,"btn-login").click()

time.sleep(3)
if "dashboard" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")


#invalid password
#open a login page
driver.get("http://localhost/complaint_management/login.php")
#Enter username
driver.find_element(By.ID,"username_or_email").send_keys("grishma@gmail.com")
#Enter password
driver.find_element(By.ID,"password").send_keys("ask@grisma")
#click on login
driver.find_element(By.CLASS_NAME,"btn-login").click()

time.sleep(3)
if "dashboard" in driver.current_url:
    print("Invalid Password:Failed")
else:
    print("Invalid Password:Successful")

#Invalid username
#open a login page
driver.get("http://localhost/complaint_management/login.php")
#Enter username
driver.find_element(By.ID,"username_or_email").send_keys("grishmathp@gmail.com")
#Enter password
driver.find_element(By.ID,"password").send_keys("ask@grishma")
#click on login
driver.find_element(By.CLASS_NAME,"btn-login").click()

time.sleep(3)
if "dashboard" in driver.current_url:
    print("Invalid Username:Login Failed")
else:
    print("Invalid Username:Login Successful")

#blank field
#open a login page
driver.get("http://localhost/complaint_management/login.php")
#Enter username
driver.find_element(By.ID,"username_or_email").send_keys("")
#Enter password
driver.find_element(By.ID,"password").send_keys("")
#click on login
driver.find_element(By.CLASS_NAME,"btn-login").click()

time.sleep(3)
if "dashboard" in driver.current_url:
    print("Blank field:Failed")
else:
    print("Blank field:successful")

#quit
driver.quit()

