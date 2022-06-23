# 1. Откройте страницу https://opensource-demo.orangehrmlive.com/ и напишите тест для логина в систему.
# Если будет ошибка логина и пароля, тогда повторите попытку через несколько часов
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
driver.quit()

# 2. Напишите тест для создания пользователя:
# Сценарий: логин в систему - > нажатие на вкладку PIM - > переход на вкладку Add Employee - > заполнение полей First и Last Name - > нажатие на кнопку
# Save(после чего происходит автоматический переход в профиль – это финальный результат)
# • Для решения этой задачи, используйте предыдущий тест для логина в систему, после него продолжайте написание новых команд (помните: driver.quit() должен
# быть в конце)
# • Чтобы элементы успели подгрузиться, перед переходом на вкладку “Add Employee”, напишите команду time.sleep(3)
# • Заполнять нужно только поля First Name, Last Name
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
pim_btn = driver.find_element_by_id("menu_pim_viewPimModule")
pim_btn.click()
time.sleep(3)
add_btn = driver.find_element_by_id("menu_pim_addEmployee")
add_btn.click()
firstname = driver.find_element_by_id("firstName")
firstname.send_keys("Иван")
lastname = driver.find_element_by_id("lastName")
lastname.send_keys("Иванов")
save_btn = driver.find_element_by_id("btnSave")
save_btn.click()
driver.quit()

# 3. Напишите тест для удаления пользователя из системы(созданного в предыдущем тесте):
# Предусловие: создан пользователь
# Сценарий: логин в систему - > нажатие на вкладку PIM - > переход на вкладку Employee List - > ввод имени и фамилии в Employee Name- > нажатие на кнопку
# Search - > нажатие на чек-бокс(селектор можно узнать вручную из предыдущего теста) - > нажатие на Delete - > нажатие на Ok в диалоговом окне
# • Для решения этой задачи, используйте тест для логина в систему, после него продолжайте написание новых команд
# • Чтобы элементы успели подгрузиться, перед вкладкой “Employee_list”, и после поиска в ней, напишите команду time.sleep(3)
# • Попробуйте использовать не более двух xpath селекторов
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
pim_btn = driver.find_element_by_id("menu_pim_viewPimModule")
pim_btn.click()
time.sleep(3)
employee_btn = driver.find_element_by_id("menu_pim_viewEmployeeList")
employee_btn.click()
employee_name = driver.find_element_by_name("empsearch[employee_name][empName]")
time.sleep(3)
employee_name.send_keys("Иван Иванов")
search_btn = driver.find_element_by_name("_search")
search_btn.click()
check_selector = driver.find_element_by_id("ohrmList_chkSelectAll")
check_selector.click()
delete_btn = driver.find_element_by_id("btnDelete")
delete_btn.click()
ok_btn = driver.find_element_by_id("dialogDeleteBtn")
ok_btn.click()
time.sleep(3)
driver.quit()

# 4. Для сайта www.rushplace.com/напишите тест, в котором добавляется 3 товара в корзину и проверяется количество товаров в корзине:
# Сценарий: зайти на сайт -> добавить любых 3 товара в корзину -> перейти в корзину -> проверить что количество товаров в корзине = 3
# • Чтобы товары успели добавиться в корзину, между их добавлением используйте time.sleep(1)
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
username_field = driver.find_element_by_id("user-name")
username_field.send_keys("standard_user")
password_field = driver.find_element_by_id("password")
password_field.send_keys("secret_sauce")
login_btn = driver.find_element_by_id("login-button")
login_btn.click()
sauce_labs_backpack = driver.find_element_by_css_selector("[data-test='add-to-cart-sauce-labs-backpack']")
sauce_labs_backpack.click()
sauce_labs_bike_light = driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
sauce_labs_bike_light.click()
sauce_labs_bolt_t_shirt = driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
sauce_labs_bolt_t_shirt.click()
cart_btn = driver.find_element_by_class_name("shopping_cart_link")
cart_btn.click()
items_count = driver.find_elements_by_class_name("item_pricebar")
if len(items_count) == 3:
    print("В корзине 3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))
driver.quit()