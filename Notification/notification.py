from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#launch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximize window
driver.maximize_window()

#open a login page
driver.get("http://localhost/complaint_management/login.php")

driver.find_element(By.ID,"username_or_email").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "btn-login").click()
time.sleep(2)

driver.get("http://localhost/complaint_management/admin/update_status.php?id=19")
driver.find_element(By.NAME,"admin_remarks").send_keys("Notification test")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(2)

driver.get("http://localhost/complaint_management/login.php")
driver.find_element(By.ID,"username_or_email").send_keys("Gahan")
driver.find_element(By.ID,"password").send_keys("ask@gahan")
driver.find_element(By.CLASS_NAME, "btn-login").click()

time.sleep(2)

driver.get("http://localhost/complaint_management/user/notifications.php")
time.sleep(2)

page_text = driver.find_element(By.TAG_NAME, "body").text

if "Notification test" in page_text:
    print("Notification test: PASS")
else:
    print("Notification test: FAIL")

driver.quit()