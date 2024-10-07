from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Firefox()
    browser.get(url)

    # Вводим данные
    browser.find_element(By.CSS_SELECTOR, "input.form-control[placeholder='Enter first name']").send_keys("Elliot")
    browser.find_element(By.CSS_SELECTOR, "input.form-control[placeholder='Enter last name']").send_keys("Alderson")
    browser.find_element(By.CSS_SELECTOR, "input.form-control[placeholder='Enter email']").send_keys("e.alderson@e-corp.com")
    time.sleep(1)
    
    # Получаем путь к файлу
    current_dir = os.path.abspath(os.path.dirname(r'C:\Windows\System32\environments\selenium_course\e.alderson.txt'))
    file_path = os.path.join(current_dir, 'e.alderson.txt')  # добавляем к этому пути имя файла 
    
    # Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "input#file[name='file']")
    file_input.send_keys(file_path)
    time.sleep(1)
    
    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

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

