# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
from random import randint


def my_func(user_list: list):
    result_list = []
    for index in range(0, len(user_list) - 1):
        if user_list[index] > user_list[index + 1]:
            result_list.append(user_list[index])
    return result_list


rand_list = [randint(1, 100) for el in range(15)]
print(rand_list)
print(my_func(rand_list))
