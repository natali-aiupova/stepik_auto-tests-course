from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    # На новой странице решить капчу для роботов, чтобы получить число с ответом

    # Считать значение для переменной x
    x  = browser.find_element_by_id("input_value").text
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
