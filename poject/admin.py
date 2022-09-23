import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def browser_code(browsertype):

    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    driver.find_element(By.NAME, "firstName").send_keys("Sri")
    driver.find_element(By.NAME, "lastName").send_keys("Ram")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
    driver.find_element(By.XPATH, "//button[@class ='oxd-button oxd-button--medium oxd-button--secondary']").click()
    driver.find_element(By.XPATH, "//div[1]/div/div[2]/div/div/div[@class='oxd-select-text-input']").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Admin')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[1]/div/div[3]//div/div[@class='oxd-select-text-input']").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Enabled')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Sri")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[contains(text(),'Sri')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']").send_keys('ramji')

    driver.find_element(By.XPATH,"//div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']").send_keys("Win1234$")
    driver.find_element(By.XPATH,"//div[2]/div/div[2]/input[@class='oxd-input oxd-input--active' and@type='password']").send_keys("Win1234$")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[1]/div/div[1]/div//input[@class='oxd-input oxd-input--active']").send_keys("ramji")
    driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
    time.sleep(5)

    cus=driver.find_element(By.XPATH, "//div[@class='oxd-table-card']//div//div[2]").text
    if cus == "ramji":
        print("successfully added")
    else:
        print("not added")

    time.sleep(5)
    driver.find_element(By.XPATH,"//i/preceding::p").click()
    driver.find_element(By.XPATH,"//a[text()='Logout']").click()

    #login new user
    driver.find_element(By.NAME, "username").send_keys("ramji")
    driver.find_element(By.NAME, "password").send_keys("Win1234$")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(20)

browser_code("chrome")
