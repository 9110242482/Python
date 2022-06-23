# Home: добавление комментария
#
# 1. Откройте http: // practice.automationtesting. in /
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку"SUBMIT"
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product/selenium-ruby/'] > h3")
selenium_ruby.click()
reviews_btn = driver.find_element_by_class_name("reviews_tab")
reviews_btn.click()
stars = driver.find_element_by_class_name("star-5")
stars.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Ivan")
email = driver.find_element_by_id("email")
email.send_keys("test@mail.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()