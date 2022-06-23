# 1. Преобразуйте переменную x, так, чтобы вывод на экран происходил без ошибки.
# • Для решения задач, используйте PyCharm или любой другой аналог.
# Подсказка: есть два варианта решения, изменить первую строку или изменить вторую
#
# Исходные данные: (используйте их для решения задачи)
# x = '25'
# print(x+25)
#
# Ожидаемый вывод:
# 50
x = 25
print(x+25)
# или
x = '25'
print(int(x)+25)
# или
x = int('25')
print(x+25)

# 2. Напишите программу, где на ввод с клавиатуры подаются два числа X и Y, после чего, на экране должна
# отобразиться сумма этих чисел.
#
# Пример ввода:
# 50
# 25
# Пример вывода:
# 75
x = int(input())
y = int(input())
print(x+y)

# 3. Напишите программу, которая будет преобразовывать общее время ночного сна человека в минуты.
# • Программа принимает с клавиатуры на вход значения X (часы) и Y(минуты).
# • На экран нужно вывести общее время сна в минутах.
# В этой и дальнейших задачах, проверяйте работу программы на всех значениях из примеров ввода.
#
# Пример ввода:     Пример ввода:       Пример ввода:
# 8                 0                   23
# 30                15                  30
# Пример вывода:    Пример вывода:      Пример вывода:
# 510               15                  1410
x = int(input())
z = x*60
y = int(input())
print(z+y)

# 4. Напишите программу, где на ввод с клавиатуры подаются буквы и цифры X и Y, после чего, на экране должны
# отобразиться данные ввода с пробелом.
#
# Пример ввода:     Пример ввода:
# abc               456
# 123               def
# Пример вывода:    Пример вывода:
# abc 123           456 def
x = input()
y = input()
print(x, y)

# 5. Напишите программу, где на ввод с клавиатуры подаются любые значения X и Y, после чего, на экране должна
# отобразиться сумма длины(количестов символов) этих значений.
#
# Пример ввода:     Пример ввода:
# Python            Текст с пробелом
# 12345             123абв
# Пример вывода:    Пример вывода:
# 11                22
x = input()
y = input()
print(len(x+y))

# 6. Напишите программу, которая объединяет первую и вторую строку и умножает их на N раз.
# Программа принимает с клавиатуры на вход три значения: первой строки, второй строки и числовое значение
# третьей строки N. Перед вводом значения, должно отображаться сообщение-подсказка(содержание на ваше
# усмотрение) что должно быть введено в эту сроку. Перед выводом ответа, также добавьте подсказку.
# Пример ввода: (с клавиатуры, значения должны вводиться на этой же строке, справа от текста подсказки)
# Ваш текст подсказки: Яблоко
# Ваш текст подсказки: Груша
# Ваш текст подсказки: 2
# Пример вывода:
# Ваш текст подсказки: ЯблокоГрушаЯблокоГруша
#
# • Обратите внимание что текст-подсказка и значения находятся на одной строке
# • Для корректного вывода, правильно расставляйте скобки "()". Правила действий, такие же как в математике.
x = input('Фрукт 1:')
y = input('Фрукт 2:')
n = int(input('Повторение фруктов:'))
print('Много фруктов:', ((x+y)*n))

# 7. Не меняя значений a,b,c,d, добавьте скобки в выражение в части print, чтобы итоговый результат выводил False.
#
# a,b,c,d = False, True, False, True
# print(a and b and not c or d)
# > True
a, b, c, d = False, True, False, True
print(a and b and (not c or d))
# или
a, b, c, d = False, True, False, True
print(a and (b and not c or d))
# или
a, b, c, d = False, True, False, True
print(a and b and not (c or d))

# 8. Напишите программу, где на ввод с клавиатуры подаются любые числовые значения, а на выводе отображается
# True или False в зависимости от того, больше первое число второго или нет.
#
# Пример ввода:     Пример ввода:
# 100               -10
# 50                50
# Пример вывода:    Пример вывода:
# True              False
x = int(input())
y = int(input())
print(x>y)

# 9. Напишите программу, где на ввод с клавиатуры, поочердёно подаются целые числа X и Y. Если их сумма
# больше числа 10, тогда должно возникнуть сообщение "Сумма больше", если сумма этих чисел меньше, тогда
# должно возникнуть сообщение "Сумма меньше", при равенстве, возникнет сообщение "Сумма равна".
# Дополнительно: попробуйте решить задачу, используя else
#
# Пример ввода:     Пример ввода:   Пример ввода:
# 7                 0               -5
# 9                 5               15
# Пример вывода:    Пример вывода:  Пример вывода:
# Сумма больше      Сумма меньше     Сумма равна
x = int(input())
y = int(input())
if x+y==10:
    print('Сумма равна')
elif x+y>10:
    print('Сумма больше')
else:
    print('Сумма меньше')

# 10. Напишите программу, где нужно ввести целое число. Если оно положительное, тогда на экран выводится
# цифра 1. Если число отрицательное, выводится -1. Если введенное число – это 0, то на экран выводится 0.
# Дополнительно: используйте не больше одного if.
#
# Пример ввода:     Пример ввода:   Пример ввода:
# 500               -250            0
# Пример вывода:    Пример вывода:  Пример вывода:
# 1                 -1              0
x = int(input())
if x>0:
    print (1)
elif x==0:
    print (0)
else:
    print(-1)

# 11. Напишите программу, где на ввод с клавиатуры, поочердёно подаются целые числа X и Y. На экран
# необходимо вывести минимальное значение из двух чисел. Если значения чисел совпадают, нужно вывести
# сообщение: "Числа совпадают".
#
# Пример ввода:     Пример ввода:   Пример ввода:
# 20                50              7
# 10                100             7
# Пример вывода:    Пример вывода:  Пример вывода:
# 10                50              Числа совпадают
x = int(input())
y = int(input())
if x>y:
    print(y)
elif x==y:
    print('Числа совпадают')
else:
    print(x)

# 12. Напишите программу, которая спрашивает у пользователя 3 вопроса: его имя, профессию и возраст. А далее,
# подставляет значения и выводит три строки с ответами.
# • При выводе данных, не забывайте про пробелы.
#
# Пример ввода:         Пример ввода:
# Андрей                Алиса
# Инженер               Дизайнер
# 30                    21
# Пример вывода:        Пример вывода:
# Имя: Андрей           Имя: Алиса
# Профессия: Инженер    Профессия: Дизайнер
# Возраст: 30           Возраст: 21
name = (input('Введите имя'))
profession = (input('Введите должность'))
age = (input('Введите возраст'))
print('Имя: '+name +'\n'+ 'Профессия: '+profession +'\n'+ 'Возраст: '+age)

# 13. Программа принимает 4 целых числа. Посчитайте сумму первых двух чисел и отдельно сумму других двух.
# Разделите первую сумму на вторую. Выведите результат на экран.
#
# Пример ввода:     Пример ввода:
# 10                5
# 10                5
# 5                 10
# 5                 10
# Пример вывода:    Пример вывода:
# 2.0               0.5
x = int(input())
y = int(input())
z = int(input())
a = int(input())
print(float((x+y)/(z+a)))

# 14. Программа принимает 3 целых числа. Нужно определить какое из них является максимальным и вывести его на
# экран. У всех трёх чисел должны быть разные значения.
#
# Пример ввода:     Пример ввода:   Пример ввода:
# 100               -1              99
# 200               0               98
# 300               9               100
# Пример вывода:    Пример вывода:  Пример вывода:
# 300               9               100
x = int(input())
y = int(input())
z = int(input())
if y<x>z:
    print(x)
elif x<y>z:
    print(y)
elif x<z>y:
    print (z)
else:
    print('У всех трех чисел должны быть разные значения')

# 15. Программа принимает 3 целых числа. Нужно определить какое из них является средним(больше одного, но
# меньше другого) и вывести его на экран. У всех трёх чисел должны быть разные значения.
#
# Пример ввода:     Пример ввода:   Пример ввода:
# 10                0               555
# 20                5               333
# 30                1               777
# Пример вывода:    Пример вывода:  Пример вывода:
# 20                1               555
x = int(input())
y = int(input())
z = int(input())
if y<x<z or z<x<y:
    print(x)
elif x<y<z or z<y<x:
    print(y)
elif x<z<y or y<z<x:
    print(z)
else:
    print('У всех трех чисел должны быть разные значения')

# 16. Напишите программу, которая принимает целое число и выводит текст, как в примере.
# Обратите внимание на наличие пробелов и точек, в ответе они также должны быть.
#
# Пример ввода:                         Пример ввода:
# 7                                     -10
# Пример вывода:                        Пример вывода:
# Следующее число для числа 7 это 8.    Следующее число для числа -10 это -9.
# Предыдущее число для числа 7 это 6.   Предыдущее число для числа -10 это -11.
x = int(input())
print('Следующее число для числа '+str(x)+ ' это '+str(x+1)+'.' +'\n'+ 'Предыдущее число для числа ' +str(x)+ ' это '+str(x-1)+'.')

# 17. Напишите программу которая будет определять, достаточно ли у пользователя денег для покупки товаров. На
# вход принимается целое число(количество денег пользователя) с сообщением подсказкой: "Сколько у Вас
# денег?". Далее, нужно определить хватит ли денег на покупку всех товаров.
# Если пользователю нужна сдача, тогда на экран нужно вывести общую стоимость товаров и далее отдельно
# строкой – сумму его сдачи. Если сдача ненужна, тогда нужно вывести сообщение:
#
# "Спасибо, что без сдачи!". В
#
# других ситуациях, сообщение о нехватке суммы.
# По условию, нужно купить: хлеб (стоит 30 рублей), молоко (стоит 50 рублей) и сыр (стоит 100 руб)
#
# Пример ввода:                 Пример ввода:               Пример ввода:
# Сколько у Вас денег? 210      Сколько у Вас денег? 180    Сколько у Вас денег? 100
# Пример вывода:                Пример вывода:              Пример вывода:
# Стоимость товаров: 180 руб    Спасибо, что без сдачи!     Недостаточно денег
# Ваша сдача: 30 руб
x = 30+50+100
y = int(input('Сколько у Вас денег?'))
if x==y:
    print('Спасибо, что без сдачи!')
elif x<y:
    print('Стоимость товаров: ' +str(x)+ ' руб.'+'\n'+'Ваша сдача: '+ str(y-x)+' руб.')
else:
    print('Недостаточно денег.')

# 18. Из передачи "Спорт" Маша узнала, что рекомендуется бегать X метров в неделю, но также, сказали, что
# бегать слишком много тоже вредно и не стоит бегать более Y метров. Сейчас Маша бегает Z метров в
# неделю. Если Маша соблюдает рекомендации передачи "Спорт", выведите сообщение "Это нормально".
# Если Маша бегает менее X метров, выведите "Слишком мало бегаете", если же более Y метров, то выведите
# "Много бегать вредно".
# • Вводимое число X всегда меньше либо равно Y
# • На вход программе в три строки подаются переменные в следующем порядке: X, Y, Z
# • Будьте внимательны при выборе операторов: < и ≤ ; > и ≥
#
# Пример ввода:     Пример ввода:           Пример ввода:
# 9000              10000                   9000
# 12000             14000                   11000
# 11000             22000                   6000
# Пример вывода:    Пример вывода:          Пример вывода:
# Это нормально     Много бегать вредно     Слишком мало бегаете
x = int(input())
y = int(input())
z = int(input())
if x>y:
    print('Ошибка ввода')
else:
    if x<=z<=y:
        print('Это нормально')
    elif z<x:
        print('Слишком мало бегаете')
    else:
        print('Много бегать вредно')