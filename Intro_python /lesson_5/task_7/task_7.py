# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json


data_firm_list = []
profit_dict = {}
loss_dict = {}
joint_profit = 0
joint_loss = 0
Name_firm_index = 0
Proceeds_index = 2
Expenditure_index = 3
with open('text file for task 7.txt') as date:
    for data_line in date:
        temp_firm_stat = [el for el in data_line.split()]
        proceeds = int(temp_firm_stat[Proceeds_index])
        expenditure = int(temp_firm_stat[Expenditure_index])
        profit = proceeds - expenditure
        if profit > 0:
            profit_dict.update({temp_firm_stat[Name_firm_index]: profit})
            joint_profit += profit
        else:
            loss_dict.update({temp_firm_stat[Name_firm_index]: profit})
            joint_loss += profit
average_profit_dict = {'average_profit': joint_profit / len(profit_dict)}
average_loss_dict = {'average_loss': joint_loss / len(loss_dict)}
data_firm_list.append(profit_dict)
data_firm_list.append(average_profit_dict)
data_firm_list.append(loss_dict)
data_firm_list.append(average_loss_dict)
with open('json file for task 7.json', 'w') as json_data:
    json.dump(data_firm_list, json_data)


