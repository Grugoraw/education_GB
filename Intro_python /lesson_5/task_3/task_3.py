# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
with open('text file for task 3.txt', 'r') as data_staff:
    counter_staff = 0
    total_amount = 0
    for line in data_staff:
        data_line = [el for el in line.split()]
        if int(data_line[1]) < 20000:
            print(data_line[0])
        counter_staff += 1
        total_amount += int(data_line[1])
print(f'Средний доход всех сотрудников {total_amount / counter_staff:.02f} руб.')
