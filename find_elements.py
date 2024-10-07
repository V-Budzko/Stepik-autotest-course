from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Useless_Data")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')

    button.click()
finally:
 
    
    alert = browser.switch_to.alert
    print(alert.text.split(":")[-1].strip())
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла