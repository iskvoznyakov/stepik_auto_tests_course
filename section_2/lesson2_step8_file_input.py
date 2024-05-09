import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "lesson2_step8_short_bio.txt")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys('Илья')
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys('Сквозняков')
    email = browser.find_element(By.NAME, "email")
    email.send_keys('test@test.ru')
    file = browser.find_element(By.NAME, "file")
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
