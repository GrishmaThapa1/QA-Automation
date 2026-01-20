from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#launch a browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


# Valid Registration

driver.get("http://localhost/complaint_management/user/register.php")
driver.find_element(By.ID,"username").send_keys("Gahan")
driver.find_element(By.ID,"email").send_keys("gahan@gmail.com")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.ID,"confirm_password").send_keys("ask@gahan")
driver.find_element(By.CLASS_NAME,"btn-register").click()

time.sleep(3)
if "login" in driver.current_url:
    print("Valid Registration: PASS")
else:
    print("Valid Registration: FAIL")


# Invalid Email

driver.get("http://localhost/complaint_management/user/register.php")
driver.find_element(By.ID,"username").send_keys("Gahan")
driver.find_element(By.ID,"email").send_keys("gahan@.com")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.ID,"confirm_password").send_keys("ask@gahan")
driver.find_element(By.CLASS_NAME,"btn-register").click()
time.sleep(3)
if "login" in driver.current_url:
    print("Invalid Email Test: FAIL")   
else:
    print("Invalid Email Test: PASS")   


# Blank username and email

driver.get("http://localhost/complaint_management/user/register.php")
driver.find_element(By.ID,"username").send_keys("")
driver.find_element(By.ID,"email").send_keys("")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.ID,"confirm_password").send_keys("ask@gahan")
driver.find_element(By.CLASS_NAME,"btn-register").click()
time.sleep(3)
if "login" in driver.current_url:
    print("Blank Username/Email Test: FAIL")
else:
    print("Blank Username/Email Test: PASS")


# Password Mismatch

driver.get("http://localhost/complaint_management/user/register.php")
driver.find_element(By.ID,"username").send_keys("Gahan")
driver.find_element(By.ID,"email").send_keys("gahan@gmail.com")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.ID,"confirm_password").send_keys("ask@gan")
driver.find_element(By.CLASS_NAME,"btn-register").click()
time.sleep(3)
if "login" in driver.current_url:
    print("Password Mismatch Test: FAIL")
else:
    print("Password Mismatch Test: PASS")

# Short Password (<6)

driver.get("http://localhost/complaint_management/user/register.php")
driver.find_element(By.ID,"username").send_keys("Gahan")
driver.find_element(By.ID,"email").send_keys("gahan@gmail.com")
driver.find_element(By.ID,"password").send_keys("ask")
driver.find_element(By.ID,"confirm_password").send_keys("ask")
driver.find_element(By.CLASS_NAME,"btn-register").click()
time.sleep(3)
if "login" in driver.current_url:
    print("Short Password Test: FAIL")
else:
    print("Short Password Test: PASS")

# Quit browser
driver.quit()
