from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math


url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Firefox()
    browser.get(url)

    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    v = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(v) # ищем элемент со значением "v" 
    time.sleep(2)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
   # Получаем текст из всплывающего окна
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    # Извлекаем код из текста всплывающего окна
    code = alert_text.split(':')[-1].strip()  # Извлекаем число после двоеточия
    print(f"Полученный код: {code}")

    # Закрываем алерт
    alert.accept()

finally:
    browser.quit()