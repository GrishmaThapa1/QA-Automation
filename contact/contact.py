from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager

#launch a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#maximize window
driver.maximize_window()

#open contact page
driver.get("http://localhost/complaint_management/contact.php")

driver.find_element(By.NAME,"name").send_keys("Grishma")
driver.find_element(By.NAME,"email").send_keys("grishma@gmail.com")
driver.find_element(By.NAME,"message").send_keys("Hello there!")
driver.find_element(By.NAME,"send_message").click()

# validation 
success_msg = driver.find_element(By.ID, "successMsg").text

if "sent successfully" in success_msg.lower():
    print("Contact form test: PASS")
else:
    print("Contact form test: FAIL")

driver.quit()

