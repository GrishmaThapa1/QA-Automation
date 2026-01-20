from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#launch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize a window
driver.maximize_window()
# LOGIN FIRST (so we can access submitcomplaint) 
driver.get("http://localhost/complaint_management/login.php")
time.sleep(1)

# Enter username
driver.find_element(By.ID, "username_or_email").send_keys("gahan@gmail.com")
# Enter password
driver.find_element(By.ID, "password").send_keys("ask@gahan")
# Click on login
driver.find_element(By.CLASS_NAME, "btn-login").click()
time.sleep(3)  

# OPEN SUBMIT COMPLAINT PAGE 
driver.get("http://localhost/complaint_management/user/submit_complaint.php")
time.sleep(2)

driver.find_element(By.ID,"subject").send_keys(" class disruption")
driver.find_element(By.ID,"complaint_text").send_keys("Construction near college gate and class disrupts due to construction noise.")
driver.find_element(By.ID, "attachment").send_keys("C:\\Users\\DELL\\OneDrive\\Desktop\\QA Automation\\img.png")



driver.find_element(By.CLASS_NAME,"btn-submit").click()
time.sleep(3)
if "dashboard" in driver.current_url:  
    print("Complaint submitted successfully!")
else:
    print("Complaint submission failed!")

#complaint submission with blank subject and complaint text
# LOGIN FIRST (so we can access submitcomplaint) 
driver.get("http://localhost/complaint_management/login.php")
time.sleep(1)

# Enter username
driver.find_element(By.ID, "username_or_email").send_keys("gahan@gmail.com")
# Enter password
driver.find_element(By.ID, "password").send_keys("ask@gahan")
# Click on login
driver.find_element(By.CLASS_NAME, "btn-login").click()
time.sleep(3)  

# OPEN SUBMIT COMPLAINT PAGE 
driver.get("http://localhost/complaint_management/user/submit_complaint.php")
time.sleep(2)

driver.find_element(By.ID,"subject").send_keys(" ")
driver.find_element(By.ID,"complaint_text").send_keys("")
driver.find_element(By.ID, "attachment").send_keys("C:\\Users\\DELL\\OneDrive\\Desktop\\QA Automation\\img.png")



driver.find_element(By.CLASS_NAME,"btn-submit").click()
time.sleep(3)
if "dashboard" in driver.current_url:  
    print("Complaint submitted successfully!")
else:
    print("Complaint submission failed!")

driver.quit()