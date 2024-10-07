from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# Запуск браузера
browser = webdriver.Firefox()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем, когда цена станет $100, до 12 секунд
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    # Ждем появления элемента с x и вычисляем результат
    x_element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'input_value')))
    x_value = x_element.text  # Извлекаем текст из элемента
    result = str(math.log(abs(12 * math.sin(int(x_value)))))

    # Вводим ответ в поле
    answer = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "answer"))
    )
    answer.send_keys(result)

    # Нажимаем на кнопку для отправки
    submit_button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    submit_button.click()

    print("Нажали на кнопку Submit, ждем алерт...")

    # Увеличиваем время ожидания до 20 секунд
    alert = WebDriverWait(browser, 20).until(EC.alert_is_present())
    alert_text = alert.text
    code = alert_text.split(':')[-1].strip()  # Извлекаем число после двоеточия
    print(f"Полученный код: {code}")

    # Закрываем алерт
    alert.accept()

finally:
    # Закрываем браузер
    browser.quit()
