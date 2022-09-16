# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
user_number = input('Введите число: ')
number_1 = int(user_number)
number_2 = int(user_number + user_number)
number_3 = int(user_number + user_number + user_number)
print(number_1 + number_2 + number_3)
