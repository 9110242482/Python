# 1.
# 1. Откройте https://opensource-demo.orangehrmlive.com
# 2. Залогиньтесь и перейдите в PIM - > Employee List
# 3. Нажмите на имя любого сотрудника (произойдёт переход в его карточку с данными)
# • если список пуст, создайте сотрудника вручную на этой же вкладке, нажав на"Add"
# 4. Добавьте проверку, что радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора
# 5. Добавьте проверку, что селектор Nationality в данный момент недоступен для выбора
# 6. В карточке сотрудника, нажмите на кнопку "Edit"
# 7. Измените пол сотрудника на противоположный
# 8. Добавьте проверку, что радиокнопка с полом сотрудника действительно выбрана
# 9. В селекторе Nationality выберите самую последнюю страну в списке
# 10. Добавьте проверку, что в селекторе Nationality выбрана последняя страна в списке
# 11. Выберите первоначальный пол сотрудника, а в селекторе Nationality выберите вариант "-- Select --"
# 12. Сохраните изменения, нажав на кнопку "Save"
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
PIM = driver.find_element_by_id("menu_pim_viewPimModule")
PIM.click()
employee = driver.find_element_by_id("menu_pim_viewEmployeeList")
employee.click()
name = driver.find_element_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(3) > a")
name.click()
female = driver.find_element_by_id("personal_optGender_2")
female_checked = female.get_attribute("disabled")
if female_checked is not None:
    print("Выбор пола не доступен")
else:
    print("Выбор пола доступен")
nationality = driver.find_element_by_id("personal_cmbNation")
nationality_checked = nationality.get_attribute("disabled")
if nationality_checked is not None:
    print("Выбор национальности не доступен")
else:
    print("Выбор национальности доступен")
edit_btn = driver.find_element_by_id("btnSave")
edit_btn.click()
female_checkbox = driver.find_element_by_id("personal_optGender_2")
female_checkbox.click()
female_checked = female.get_attribute("checked")
if female_checked is not None:
    print("Женский пол выбран")
else:
    print("Женский пол не выбран")
driver.find_element_by_id("personal_cmbNation").click()
nat_Zimbabwean = driver.find_element_by_css_selector("#personal_cmbNation > option[value='193']")
nat_Zimbabwean.click()
driver.find_element_by_id("personal_cmbNation").click()
Zimbabwean_selected = nat_Zimbabwean.get_attribute("selected")
if Zimbabwean_selected is None:
    print("Zimbabwean не выбран")
else:
    print("Zimbabwean выбран")
male = driver.find_element_by_id("personal_optGender_1")
male.click()
nat_Select = driver.find_element_by_css_selector("#personal_cmbNation > option[value='0']")
nat_Select.click()
edit_btn.click()
driver.quit()

# 2.
# 1. Настройте открытие окон в полный размер, с помощью команды из предыдущего урока: driver.maximize_window()
# • Для большей стабильности тестов, рекомендуется использовать её и в дальнейшем, указав сразу после инициализации драйвера: driver = webdriver.Chrome()
# 2. Откройте страницу http://demo.automationtesting.in/Register.html
# 3. Заполните произвольными данными только обязательные поля(*) в регистрации(а так же поля: Date of Birth, Password, Confirm Password)
# • Поле телефон должно содержать: 10 цифр, без +, например: 1234567890 ; если номер уже существует в системе – появится ошибка
# • Значение в селекторе country, date of birth выбирайте с помощью класса Select из библиотеки WebDriver
# • Поля password, confirm password должны содержать: не менее 6 символов, маленькую букву, большую букву, цифру
# 4. Загрузите любой файл в раздел "Photo" вверху справа
# 5. Проскролльте страницу вниз на 300 пикселей
# 6. Нажмите на кнопку Submit # если после нажатия на кнопку не происходит переход на следующую страницу, тогда завершите задание на этом шаге(иногда бывает, что она не работает)
# 7. Добавьте проверку, что произошёл переход на страницу: http://demo.automationtesting.in/WebTable.html
# • Дополнительно: улучшите проверку таким образом, чтобы в консоли выводилось содержательное сообщение, из которого можно понять, на какой странице находимся
# сейчас и на какой странице ожидаем находиться.
#
# • Не забывайте использовать time.sleep() если нужно
# • В задании можно иногда использовать XPATH (пример структуры: //тег[@атрибут='значение']
# • Будет также полезно вспомнить про составной селектор (пример структуры: .class .other class) ; (пример структуры 2: #someid .someclass)
# • Ещё здесь может пригодиться nth-child() (пример структуры: element:nth-child(порядковый номер)
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
first_name = driver.find_element_by_css_selector("[placeholder='First Name']")
first_name.send_keys("Ivan")
last_name = driver.find_element_by_css_selector("[placeholder='Last Name']")
last_name.send_keys("Ivanov")
email_address = driver.find_element_by_css_selector("[ng-model='EmailAdress']")
email_address.send_keys("test@mail.ru")
phone = driver.find_element_by_css_selector("[ng-model='Phone']")
phone.send_keys("5678924513")
gender = driver.find_element_by_css_selector("[value='Male']")
gender.click()
countries = driver.find_element_by_css_selector("#countries>option[value]")
countries.click()
country = driver.find_element_by_css_selector("#country>option[value='Hong Kong']")
country.click()
year = driver.find_element_by_css_selector("#yearbox>option[value='2001'")
year.click()
month = driver.find_element_by_css_selector("[placeholder='Month']>option[value='August']")
month.click()
day = driver.find_element_by_css_selector("#daybox>option[value='23']")
day.click()
password = driver.find_element_by_css_selector("[ng-model='Password']")
password.send_keys("111111aA")
confirm = driver.find_element_by_css_selector("[ng-model='CPassword']")
confirm.send_keys("111111aA")
file = ('C:\e2.jpeg')
photo = driver.find_element_by_id("imagesrc")
photo.send_keys(file)
driver.execute_script("window.scrollBy(0, 300);")
submit_btn = driver.find_element_by_id("submitbtn")
submit_btn.click()
current_page = driver.current_url
expected_address = "http://demo.automationtesting.in/WebTable.html"
if current_page == expected_address:
    print("Адрес страницы совпадает")
else:
    print("Адрес не совпадает, текущий:",current_page,", ожидаемый:", expected_address)
driver.quit()

# 3.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Перейдите на вкладку "SwitchTo" - > "Alerts"
# • Здесь используйте клики(их будет 2) вместо выбора по селектору
# • Если не получится перейти на вкладку Alerts, тогда откройте страницу http://demo.automationtesting.in/Alerts.html и выполняйте задание начиная с 3-го шага
# 3. Нажмите на кнопку "click the button to display an alert box:" # перед нажатием добавьте паузу
# 4. Выведите в консоль содержимое окна alert и нажмите "OK"
# • Дополнительно(если получится): добавьте тест, что содержимое равно тексту "I am an alert box!" , а если не равно, тогда в консоли выводится сообщение об ошибке
# 5. Получите адрес текущей ссылки
# 6. Откройте новую вкладку в браузере, введите ссылку из предыдущего шага и перейдите по ней # перед открытием добавьте паузу
# 7. Нажмите на "Alert with OK & Cancel" -> "click the button to display a confirm box" # перед нажатием добавьте паузу
# 8. В модальном окне нажмите "Отмена"
# 9. Откройте новую вкладку в браузере, введите ссылку из шага 5 и перейдите по ней # перед открытием добавьте паузу
# 10. Нажмите на "Alert with Textbox"-> "click the button to demonstrate the prompt box" # перед нажатием добавьте паузу
# 11. В модальном окне, введите текст: "Ура! Задание выполнено!" и нажмите "OK"
#
# • Если вдруг никак не будет получаться переключаться между окнами браузера, выполните всё задание в одном окне
# • Если считаете, что селектор подобран правильно и почему-то не срабатывает, используйте между командами time.sleep(5)
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/WebTable.html")
switchto = driver.find_element_by_css_selector("[href='SwitchTo.html']")
switchto.click()
alerts = driver.find_element_by_css_selector("[href='Alerts.html']")
alerts.click()
driver.get("http://demo.automationtesting.in/Alerts.html")
alert_btn = driver.find_element_by_class_name("btn-danger")
time.sleep(3)
alert_btn.click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
current_text = alert_text
expected_text = "I am an alert box!"
if current_text == expected_text:
    print("Текст верный")
else:
    print("Текст неверный, текущий:",current_text,", ожидаемый:", expected_text)
alert.accept()
current_page = driver.current_url
print(current_page)
time.sleep(3)
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get(current_page)
ok_cancel = driver.find_element_by_css_selector("[href='#CancelTab']")
ok_cancel.click()
click_btn = driver.find_element_by_class_name("btn-primary")
time.sleep(3)
click_btn.click()
confirm = driver.switch_to.alert
confirm.dismiss()
time.sleep(3)
driver.execute_script("window.open();")
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
driver.get(current_page)
textbox = driver.find_element_by_css_selector("[href='#Textbox']")
textbox.click()
click_btn_box = driver.find_element_by_class_name("btn-info")
time.sleep(3)
click_btn_box.click()
prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()
driver.quit()

# 4.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Перейдите в раздел "More" -> "Loader"
# 3. Реализуйте явное ожидание(EC) для отображения текста "Run"
# 4. Нажмите кнопку "Run"
# 5. Реализуйте явное ожидание(EC) что слово "Lorem" содержится в тексте модального окна
# 6. Реализуйте явное ожидание(EC) для нажатия в модальном окне на кнопку "Save Changes" и нажмите на неё
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")
more = driver.find_element_by_css_selector("[href='#']")
more.click()
loader = driver.find_element_by_css_selector("[href='Loader.html']")
loader.click()
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "loader"), "Run"))
run_btn = driver.find_element_by_id("loader")
run_btn.click()
WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "modal-body"), "Lorem"))
save_changes_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick='history.go(0)']")))
save_changes_btn.click()
driver.quit()

# 5.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "Dynamic Data"
# • Здесь и в дальнейших заданиях используйте клики(их будет 2) вместо выбора по селектору
# 4. Добавьте проверку, что заголовок окна равен "Loading the data Dynamically"
# 5. Нажмите на кнопку "Get Dynamic Data"
# 6. Выведите в консоли адрес ссылки, которая сгенерируется в теге img (похожий на: https://randomuser.me/api/portraits/...)
# • Чтобы это сделать, используйте метод .get_attribute("атрибут")
# • Если адрес ссылки сильно отличается от примера в шаге 6, тогда после нажатия на кнопку из шага 5 добавьте паузу time.sleep(3)
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")
more = driver.find_element_by_css_selector("[href='#']")
more.click()
dindate = driver.find_element_by_css_selector("[href='DynamicData.html']")
dindate.click()
wind_name = driver.find_element_by_css_selector(".cont_box_center>h3")
wind_name_get_text = wind_name.text
assert wind_name_get_text == "Loading the data Dynamically"
save_btn = driver.find_element_by_id("save")
save_btn.click()
img = driver.find_element_by_css_selector("#loading>img")
img_site = img.get_attribute("src")
print(img_site)
driver.quit()

# 6.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "File Upload"
# 4. Загрузите файл с картинкой
# 5. Нажмите на кнопку "Remove"
# 6. Загрузите пустой файл с расширением .txt (можно создать в блокноте)
# 7. Закройте появившееся красное сообщение об ошибке
# • Дополнительно(если получится): добавьте проверку что кнопка upload недоступна для нажатия
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")
more = driver.find_element_by_css_selector("[href='#']")
more.click()
upload = driver.find_element_by_css_selector("[href='FileUpload.html']")
upload.click()
file = ('C:\e2.jpeg')
upload_file = driver.find_element_by_id("input-4")
upload_file.send_keys(file)
remove = driver.find_element_by_css_selector(".fileinput-remove-button")
remove.click()
file_2 = ('C:\doc.txt')
upload_file_2 = driver.find_element_by_id("input-4")
upload_file_2.send_keys(file_2)
close = driver.find_element_by_css_selector(".kv-error-close")
close.click()
upload_btn = driver.find_element_by_css_selector(".fileinput-upload-button")
upload_btn_able = upload_btn.get_attribute("disabled")
if upload_btn_able is not None:
    print("Кнопка Upload недоступна для нажатия")
else:
    print("Кнопка Upload доступна для нажатия")
driver.quit()

# 7.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "JQuery ProgressBar"
# 4. Реализуйте явное ожидание(EC) для проверки что кнопка "Close" невидима
# • Для этого, предварительно вручную нажмите на кпоку "Start Download" и в появившемся окне возьмите селектор кнопки "Close"
# 5. Нажмите кнопку "Start Download"
# 6. Реализуйте явное ожидание(EC) для проверки что кнопка называется "Cancel Download"
# 7. Закройте окно. Снова откройте
# 8. Реализуйте явное ожидание(EC) для проверки что в окне присутствует текст "Complete!"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")
more = driver.find_element_by_css_selector("[href='#']")
more.click()
jquery = driver.find_element_by_css_selector("[href='JqueryProgressBar.html']")
jquery.click()
close = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog-buttonset>button")))
start_btn = driver.find_element_by_id("downloadButton")
start_btn.click()
WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset>button"), "Cancel Download"))
close_btn = driver.find_element_by_css_selector(".ui-dialog-buttonset>button")
close_btn.click()
start_btn = driver.find_element_by_id("downloadButton")
start_btn.click()
WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "progress-label"), "Complete!"))
driver.quit()

# 8.
# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "Switch to" -> "Windows"
# 4. В разделе "Open New Tabbed Windows" нажмите кнопку "click"
# 5. Переключите драйвер на вторую вкладку - > закройте её -> переключитесь обратно на первую вкладку
# • Чтобы закрыть вкладку: после переключения на неё на новой строке добавьте команду driver.close()
# 6. Перейдите в раздел "Separate Multiple Windows" и нажмите "click"
# 7. Переключите драйвер на вторую вкладку # здесь нужно будет использовать handles[2], тк ранее закрытая вкладка с шага 4 останется в
# памяти
# 8. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Index.html"
# 9. Используя явное ожидание(EC), проверьте что в браузере открыто 3 вкладки, выведите в консоли результат проверки (True/False)
# 10. В поле "email" напишите любую почту и нажмите на кнопку в виде ">" справа от поля
# 11. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Register.html"
# • Дополнительно(необязательно): для всех EC, вынесите часть проверки в переменную (как на последнем слайде перед практикой)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.implicitly_wait(5)
switchto = driver.find_element_by_css_selector("[href='SwitchTo.html']")
switchto.click()
windows = driver.find_element_by_css_selector("[href='Windows.html']")
windows.click()
tabbed_click = driver.find_element_by_css_selector("[href='http://www.selenium.dev']>button")
tabbed_click.click()
second_browser_tab = driver.window_handles[1]
driver.switch_to.window(second_browser_tab)
driver.close()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
seperate = driver.find_element_by_css_selector("[href='#Multiple']")
seperate.click()
seperate_click = driver.find_element_by_css_selector("#Multiple>.btn-info")
seperate_click.click()
second_browser_tab = driver.window_handles[1]
driver.switch_to.window(second_browser_tab)
third_browser_tab = driver.window_handles[2]
driver.switch_to.window(third_browser_tab)
wait = WebDriverWait(driver, 10)
link_check = wait.until(EC.url_to_be("http://demo.automationtesting.in/Index.html"))
number_of_tabs = wait.until(EC.number_of_windows_to_be(3))
print(number_of_tabs )
email = driver.find_element_by_id("email")
email.send_keys("test")
email_btn = driver.find_element_by_id("enterimg")
email_btn.click()
link_check = wait.until(EC.url_to_be("http://demo.automationtesting.in/Register.html"))
driver.quit()