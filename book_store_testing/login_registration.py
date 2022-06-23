# Registration_login: регистрация аккаунта
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
email_address = driver.find_element_by_id("reg_email")
email_address.send_keys("mar-rin-na@yandex.ru")
time.sleep(5)
password = driver.find_element_by_id("reg_password")
password.send_keys("mar-rin-na@yandex.ru")
register_btn = driver.find_element_by_css_selector("[value='Register']")
register_btn.click()
driver.quit()

# Registration_login: логин в систему
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
email_address_login = driver.find_element_by_id("username")
email_address_login.send_keys("mar-rin-na@yandex.ru")
password_login = driver.find_element_by_id("password")
password_login.send_keys("mar-rin-na@yandex.ru")
login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
element = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")
element_get_text = element.text
assert element_get_text == "Logout"
driver.quit()