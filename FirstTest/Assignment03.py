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
    driver.get("https://github.com/")
    sign_in = driver.find_element_by_link_text("Sign in")
    sign_in.click()
    print(sign_in)
    w = WebDriverWait(driver, 3)
    w.until(EC.presence_of_all_elements_located((By.ID,"login_field")))
    print("Page load happened")

    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    print("UserName Password Entered.. Logging in")
    driver.find_element_by_name("commit").click()
    time.sleep(5)
    print("Waiting for Page Loading")

    w = WebDriverWait(driver, 3)
    w.until(EC.presence_of_all_elements_located((By.ID,"dashboard-repos-filter-left")))
    print("Page load happened.. Interacting with Static Elements")
    time.sleep(2)
    print("Find Stable Component First")
    repos_container = driver.find_element_by_class_name("js-repos-container")
    print("Accessing List Element with Dynamic Content")
    repo_list_ul = repos_container.find_element_by_class_name("list-style-none")
    items = repo_list_ul.find_elements_by_tag_name("li")
    for item in items:
        text = item.text
        print(text)
    time.sleep(2)
    print("Accessing search field - static component with ID")

    driver.find_element_by_id("dashboard-repos-filter-left").send_keys("javarishi")
    time.sleep(2)

    print("Accessing List Again")
    repo_list_ul = repos_container.find_element_by_class_name("list-style-none")
    items = repo_list_ul.find_elements_by_tag_name("li")
    for item in items:
        text = item.text
        print(text)
    time.sleep(2)

    print("Xpath Vs CSS Class Selector - For Same Element")
    search_withxpath = driver.find_element_by_xpath("//*[contains(@class,'js-site-search-form')]/label/input")
    print("Accessing Element with XPath ", search_withxpath)
    search_withCSS = driver.find_element_by_class_name("js-site-search-focus")
    print("Accessing Element with CSS Class ", search_withCSS)
    static_xpath = driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/div[1]/div[1]/form/label/input")
    print("Accessing Element with Static XPath ", static_xpath)
except Exception as ex:
    print("Error while doing operation", ex)
finally:
    driver.close()
