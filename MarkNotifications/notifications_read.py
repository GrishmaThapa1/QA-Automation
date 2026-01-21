from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#launch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open a login page
driver.get("http://localhost/complaint_management/login.php")
driver.find_element(By.ID,"username_or_email").send_keys("Gahan")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.CLASS_NAME,"btn-login").click()
time.sleep(2)

#open notification page
driver.get("http://localhost/complaint_management/user/notifications.php")
time.sleep(2)

#validation
try:
    driver.find_element(By.CSS_SELECTOR,"li.unread .mark-read-btn").click()
    time.sleep(2)
    print("Notication Mark as Read:PASS")
   
except:
    print("Notification Mark as Read:FAIL")
driver.quit()