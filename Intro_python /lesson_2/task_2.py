#  Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
#  0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
len_my_list = int(input('Введите длинну списка: '))
for index in range(0, len_my_list):
    my_list.append(int(input('Введите элементы списка: ')))
print(my_list)
for index in range(1, len_my_list, 2):
    print(index)
    temp = my_list[index]
    my_list[index] = my_list[index - 1]
    my_list[index - 1] = temp
print(my_list)
