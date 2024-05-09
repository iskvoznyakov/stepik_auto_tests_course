from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    second_number = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    total = first_number + second_number

    spisok = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    spisok.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
