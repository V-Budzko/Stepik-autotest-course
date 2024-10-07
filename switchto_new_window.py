from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)
    time.sleep(1)

    # Нажимаем на кнопку, чтобы произошло перенаправление на новую вкладку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Ждем, пока элемент с id 'input_value' станет доступен, и получаем его текст
    x_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input_value'))).text

    # Вычисляем результат
    result = str(math.log(abs(12 * math.sin(int(x_element)))))

    # Вводим результат в поле
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(result)
    time.sleep(1)

    # Нажимаем кнопку для отправки
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

    # Переключаемся на алерт и получаем его текст
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_text = alert.text
    code = alert_text.split(':')[-1].strip()  # Извлекаем число после двоеточия
    print(f"Полученный код: {code}")

    # Закрываем алерт
    alert.accept()

finally:
    # Закрываем браузер через 5 секунд
    time.sleep(5)
    browser.quit()
