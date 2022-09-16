# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint


with open('text file for task 5.txt', 'w') as data:
    data.write(' '.join(str(randint(0, 100))for el in range(5)))
with open('text file for task 5.txt', 'r') as data:
    for line in data:
        result_list = line.split()
result = 0
for num in result_list:
    result += int(num)
print(result)
