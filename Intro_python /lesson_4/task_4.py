# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив
# чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randint

# Решение 1
rand_list = [randint(1, 20) for el in range(15)]
print(rand_list)
result_list = []
for el in rand_list:
    counter = 0
    for check in rand_list:
        if el == check:
            counter += 1
    if counter < 2:
        result_list.append(el)
print(result_list)

# Решение 2
rand_list_2 = [randint(1, 20) for el in range(15)]
print(rand_list_2)
check_dict = {}
result_list_2 = []
for el in rand_list_2:
    if str(el) in check_dict:
        check_dict[str(el)] += 1
    else:
        check_dict.update({str(el): 1})
for el in check_dict:
    if check_dict[el] == 1:
        result_list_2.append(str(el))
print(result_list_2)
