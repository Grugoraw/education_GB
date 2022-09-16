# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета необязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def int_func(val: str):
    new_str = ''
    for symbol in val:
        if symbol.isdigit():
            new_str += symbol
        else:
            break
    return int(new_str)


education_stat = {}
with open('text file for task 6.txt') as education_date:
    for line in education_date:
        temp_list = line.split()
        total_hours = 0
        for index in range(1, len(temp_list)):
            if temp_list[index] != '—':
                total_hours += int_func(temp_list[index])
        discipline = temp_list[0]
        discipline = discipline[:len(discipline) - 1]
        education_stat.update({discipline: total_hours})
print(education_stat)

