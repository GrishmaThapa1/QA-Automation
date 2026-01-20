from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#launch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximize window
driver.maximize_window()

#open login page
driver.get("http://localhost/complaint_management/login.php")

driver.find_element(By.ID,"username_or_email").send_keys("admin")
driver.find_element(By.ID,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"btn-login").click()
time.sleep(3)

driver.get("http://localhost/complaint_management/admin/update_status.php?id=21")
time.sleep(2)

driver.find_element(By.NAME,"admin_remarks").send_keys("complaint resolved successfully.Thank you for trusting us!")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(3)
if "view_complaints" in driver.current_url:
    print("Update status:Pass")
else:
    print("Update status:Fail")
