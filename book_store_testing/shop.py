# Shop: отображение страницы товара
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "HTML 5 Forms"
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
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
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
book = driver.find_element_by_css_selector(".woocommerce-LoopProduct-link>[title='Mastering HTML5 Forms']")
book.click()
element = driver.find_element_by_class_name("product_title")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
driver.quit()

# Shop: количество товаров в категории
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара
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
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
html = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']")
html.click()
book_item = driver.find_elements_by_class_name("attachment-shop_catalog")
assert len(book_item) == 3
driver.quit()

# Shop: сортировка товаров
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
# 5. Отсортируйте товары от большего к меньшему
# • в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
# • Используйте проверку по value
import time
from selenium.webdriver.support.select import Select
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
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
selector = driver.find_element_by_css_selector("[value='menu_order']")
default_sorting = selector.get_attribute("selected")
assert default_sorting is not None
selector_price = driver.find_element_by_class_name("orderby")
select = Select(selector_price)
select.select_by_value("price-desc")
sort_by_price = driver.find_element_by_css_selector("[value='price-desc']")
high_to_low = sort_by_price.get_attribute("selected")
assert high_to_low is not None
driver.quit()

# Shop: отображение, скидка товара
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
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
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
book_android = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
book_android.click()
old_price = driver.find_element_by_css_selector(".price > del >.woocommerce-Price-amount")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price > ins >.woocommerce-Price-amount")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
bookcover = driver.find_element_by_class_name("wp-post-image")
bookcover.click()
time.sleep(5)
bookcoler_close = driver.find_element_by_class_name("pp_close")
bookcoler_close.click()
driver.quit()

# Shop: проверка цены в корзине
#
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

# если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# если все книги будут out of stock - тогда пропустите это и следующие два задания
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
add_html5 = driver.find_element_by_css_selector(".post-182 .button")
add_html5.click()
time.sleep(5)
basket_item = driver.find_element_by_css_selector("#wpmenucartli .cartcontents")
basket_item_get_text = basket_item.text
assert basket_item_get_text == "1 Item"
basket_price = driver.find_element_by_css_selector("#wpmenucartli .amount")
basket_price_get_text = basket_price.text
assert basket_price_get_text == "₹180.00"
basket = driver.find_element_by_class_name("cartcontents")
basket.click()
subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "Subtotal"))
total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "Total"))
driver.quit()

# Shop: работа в корзине

# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5 = driver.find_element_by_css_selector(".post-182 .button")
add_html5.click()
time.sleep(5)
add_jsdata = driver.find_element_by_css_selector(".post-180 .button")
add_jsdata.click()
time.sleep(5)
basket = driver.find_element_by_class_name("cartcontents")
basket.click()
time.sleep(5)
del_book = driver.find_element_by_css_selector(".product-remove> [data-product_id='180']")
del_book.click()
undo = driver.find_element_by_css_selector(".woocommerce-message > [href]")
undo.click()
quantity = driver.find_element_by_css_selector(".quantity > [name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity.clear()
quantity.send_keys("3")
update_basket_btn = driver.find_element_by_css_selector("[value='Update Basket']")
update_basket_btn.click()
jsdata_quantity = quantity.get_attribute("value")
assert jsdata_quantity == "3"
time.sleep(5)
apply_btn = driver.find_element_by_css_selector("[value='Apply Coupon']")
apply_btn.click()
message = driver.find_element_by_class_name("woocommerce-error")
message_get_text = message.text
assert message_get_text == "Please enter a coupon code."
driver.quit()

# Shop: покупка товара
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5 = driver.find_element_by_css_selector(".post-182 .button")
add_html5.click()
time.sleep(5)
basket = driver.find_element_by_class_name("cartcontents")
basket.click()
checkout_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button")))
checkout_btn.click()
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Ivan")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ivanov")
email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("mar-rin-na@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+79210000000")
country = driver.find_element_by_id("select2-chosen-1")
country.click()
country_find = driver.find_element_by_id("s2id_autogen1_search")
country_find.send_keys("russia")
country_selector = driver.find_element_by_css_selector("#select2-results-1 >.select2-results-dept-0")
country_selector.click()
street = driver.find_element_by_id("billing_address_1")
street.send_keys("Leningradskaya")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("101000")
state = driver.find_element_by_id("billing_state")
state.send_keys("No")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_payment = driver.find_element_by_id("payment_method_cheque")
check_payment.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
thank_you= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".csstransitions"), "Thank you. Your order has been received."))
payment_method= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table"), "Check Payments"))
driver.quit()