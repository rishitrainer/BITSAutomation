from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# Website credentials
username = "rishi.arun@yahoo.com"
password = "Aad@13Aug"
driver = webdriver.Firefox(executable_path=r'\PYTHON05\geckodriver-v0.29.0-win64\geckodriver.exe')
try:
    executable_path='//PYTHON05//geckodriver-v0.29.0-win64//geckodriver.exe'
    driver.get("https://github.com/")
    sign_in = driver.find_element_by_link_text("Sign in")
    sign_in.click()
    print(sign_in)
    w = WebDriverWait(driver, 8)
    w.until(EC.presence_of_all_elements_located((By.ID,"login_field")))
    print("Page load happened")

    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    print("UserName Password Entered.. Logging in")
    driver.find_element_by_name("commit").click()

    time.sleep(5)
except Exception as ex:
    print("Error while doing operation", ex)
finally:
    driver.close()
