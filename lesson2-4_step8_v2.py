from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_css_selector("button.btn").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    y = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("#solve").click()

    # Копируем результат
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

    # Нажимаем на кноку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
    browser.get("https://stepik.org/catalog?auth=login")

    # Ждем пока поле для ввода email станет кликабельным
    WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "id_login_email"))
        )

    browser.find_element_by_id("id_login_email").send_keys("почта")
    browser.find_element_by_id("id_login_password").send_keys("пароль")
    browser.find_element_by_css_selector(".sign-form__btn").click()

    # Дожидаемся пока будет обнаружен элемент с картинкой профиля (чтобы авторизация прошла)
    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )

    browser.get("https://stepik.org/lesson/181384/step/8")

    # Ждем пока появится текстовое поле
    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
        )

    # Находим поле для ввода ответа
    textarea = browser.find_element_by_css_selector(".textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)

    # Напишем текст ответа в найденное поле
    textarea.send_keys(addToClipBoard)

    # Отправляем ответ
    browser.find_element_by_css_selector(".submit-submission").click()
    
    WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "attempt__wrapper_next-link"))
        )

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
