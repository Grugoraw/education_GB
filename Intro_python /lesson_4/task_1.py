# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


script_name, working_time, hourly_pay, premium = argv
print(argv)
salary = int(working_time) * int(hourly_pay) + int(premium)
print(salary)
