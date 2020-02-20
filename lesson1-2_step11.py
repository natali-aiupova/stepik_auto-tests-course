import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. 
# Ищем кнопку для авторизации
submit_button = driver.find_element_by_css_selector(".navbar__auth")
submit_button.click()


# Метод find_element_by_id позволяет найти нужный элемент на сайте по id. 
# Ищем поле для ввода email и заполняем его
s_username = driver.find_element_by_id("id_login_email")
s_username.send_keys("почта")

# Ищем поле для ввода пароля и заполняем его
s_password = driver.find_element_by_id("id_login_password")
s_password.send_keys("пароль")

# Ищем кнопку для авторизации и заполняем ее
button = driver.find_element_by_css_selector(".sign-form__btn")

button.click()
time.sleep(10)
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
