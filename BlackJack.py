import time
from selenium import webdriver
import random
driver = webdriver.Chrome()
driver.get("https://qa-demo.kdev2.cone.ee/")
driver.maximize_window()
key = driver.find_element_by_id("api-key-field")
key.send_keys("afeb796e-b2b4-41cd-80e2-f0c86f1a8b8b")
connect_btn = driver.find_element_by_id("api-key-button")
connect_btn.click()
time.sleep(3)
game_name = driver.find_element_by_id("game_name")
game_name.send_keys("тест")
game_v2_btn = driver.find_element_by_id("start_ng_button1")
game_v2_btn.click()
time.sleep(3)
card = driver.find_elements_by_css_selector("#mainfield .btn-success")
dealer_card = random.choice(card)
dealer_card_get_text = dealer_card.text
if "2" in dealer_card_get_text:
    card_value = int(2)
elif "3" in dealer_card_get_text:
    card_value = int(3)
elif "4" in dealer_card_get_text:
    card_value = int(4)
elif "5" in dealer_card_get_text:
    card_value = int(5)
elif "6" in dealer_card_get_text:
    card_value = int(6)
elif "7" in dealer_card_get_text:
    card_value = int(7)
elif "8" in dealer_card_get_text:
    card_value = int(8)
elif "9" in dealer_card_get_text:
    card_value = int(9)
elif "10" or "J" or "Q" or "K" in dealer_card_get_text:
    card_value = int(10)
elif "A" in dealer_card_get_text:
    card_value = int(11)
dealer_card.click()
print(card_value)
total = card_value
time.sleep(3)
card2 = driver.find_elements_by_css_selector("#mainfield .btn-success")
dealer_card2 = random.choice(card2)
dealer_card2_get_text = dealer_card2.text
if "2" in dealer_card2_get_text:
    card_value2 = int(2)
elif "3" in dealer_card2_get_text:
    card_value2 = int(3)
elif "4" in dealer_card2_get_text:
    card_value2 = int(4)
elif "5" in dealer_card2_get_text:
    card_value2 = int(5)
elif "6" in dealer_card2_get_text:
    card_value2 = int(6)
elif "7" in dealer_card2_get_text:
    card_value2 = int(7)
elif "8" in dealer_card2_get_text:
    card_value2 = int(8)
elif "9" in dealer_card2_get_text:
    card_value2 = int(9)
elif "10" or "J" or "Q" or "K" in dealer_card2_get_text:
    card_value2 = int(10)
elif "A" in dealer_card2_get_text and card_value > 10:
    card_value2 = int(1)
else:
    card_value2 = int(11)
dealer_card2.click()
print(card_value2)
total = total + card_value2
print("Итог: " + str(total))
driver.execute_script("window.scrollBy(0, -100);")
time.sleep(3)
dealer_inf2 = driver.find_element_by_css_selector("#mainfield :nth-child(5)")
text2 = dealer_inf2.text
print(text2)
if total < 17 and 'Dealer thinks he stopped at: -1' in text2:
    print("С шагами диллера все ок")
elif total == 17 and 'Dealer thinks he stopped at: 17' in text2:
    print("С шагами диллера все ок")
elif total == 18 and 'Dealer thinks he stopped at: 18' in text2:
    print("С шагами диллера все ок")
elif total == 19 and 'Dealer thinks he stopped at: 19' in text2:
    print("С шагами диллера все ок")
elif total == 20 and 'Dealer thinks he stopped at: 20' in text2:
    print("С шагами диллера все ок")
elif total == 21 and 'Dealer thinks he stopped at: 21' in text2:
    print("С шагами диллера все ок")
elif total == 22 and 'Dealer thinks he stopped at: 22' in text2:
    print("С шагами диллера все ок")
elif total == 23 and 'Dealer thinks he stopped at: 23' in text2:
    print("С шагами диллера все ок")
elif total == 24 and 'Dealer thinks he stopped at: 24' in text2:
    print("С шагами диллера все ок")
elif total == 25 and 'Dealer thinks he stopped at: 25' in text2:
    print("С шагами диллера все ок")
else:
    print("Ошибка в количестве шагов диллера")
dealer_inf = driver.find_element_by_css_selector("#mainfield :nth-child(3)")
text = dealer_inf.text
print(text)
if total < 17 and 'Dealer wants card: true' in text:
    print("С желанием диллера все ок")
elif total >= 17 and 'Dealer wants card: false' in text:
    print("С желанием диллера все ок. Игра окончена")
else:
    print("Ошибка в желании диллера")
while total < 17:
    time.sleep(3)
    card2 = driver.find_elements_by_css_selector("#mainfield .btn-success")
    dealer_card2 = random.choice(card2)
    dealer_card2_get_text = dealer_card2.text
    if "2" in dealer_card2_get_text:
        card_value2 = int(2)
    elif "3" in dealer_card2_get_text:
        card_value2 = int(3)
    elif "4" in dealer_card2_get_text:
        card_value2 = int(4)
    elif "5" in dealer_card2_get_text:
        card_value2 = int(5)
    elif "6" in dealer_card2_get_text:
        card_value2 = int(6)
    elif "7" in dealer_card2_get_text:
        card_value2 = int(7)
    elif "8" in dealer_card2_get_text:
        card_value2 = int(8)
    elif "9" in dealer_card2_get_text:
        card_value2 = int(9)
    elif "10" or "J" or "Q" or "K" in dealer_card2_get_text:
        card_value2 = int(10)
    elif "A" in dealer_card2_get_text and card_value > 10:
        card_value2 = int(1)
    else:
        card_value2 = int(11)
    dealer_card2.click()
    print(card_value2)
    total = total + card_value2
    print(("Итог: " + str(total + card_value2)))
    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(3)
    dealer_inf2 = driver.find_element_by_css_selector("#mainfield :nth-child(5)")
    text2 = dealer_inf2.text
    print(text2)
    if total < 17 and 'Dealer thinks he stopped at: -1' in text2:
        print("С шагами диллера все ок")
    elif total == 17 and 'Dealer thinks he stopped at: 17' in text2:
        print("С шагами диллера все ок")
    elif total == 18 and 'Dealer thinks he stopped at: 18' in text2:
        print("С шагами диллера все ок")
    elif total == 19 and 'Dealer thinks he stopped at: 19' in text2:
        print("С шагами диллера все ок")
    elif total == 20 and 'Dealer thinks he stopped at: 20' in text2:
        print("С шагами диллера все ок")
    elif total == 21 and 'Dealer thinks he stopped at: 21' in text2:
        print("С шагами диллера все ок")
    elif total == 22 and 'Dealer thinks he stopped at: 22' in text2:
        print("С шагами диллера все ок")
    elif total == 23 and 'Dealer thinks he stopped at: 23' in text2:
        print("С шагами диллера все ок")
    elif total == 24 and 'Dealer thinks he stopped at: 24' in text2:
        print("С шагами диллера все ок")
    elif total == 25 and 'Dealer thinks he stopped at: 25' in text2:
        print("С шагами диллера все ок");
    else:
        print("Ошибка в количестве шагов диллера")
    dealer_inf = driver.find_element_by_css_selector("#mainfield :nth-child(3)")
    text = dealer_inf.text
    print(text)
    if total < 17 and 'Dealer wants card: true' in text:
        print("С желанием диллера все ок")
    elif total >= 17 and 'Dealer wants card: false' in text:
        print("С желанием диллера все ок. Игра окончена")
    else:
        print("Ошибка в желании диллера")