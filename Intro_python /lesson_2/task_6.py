# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
products_list = []
amount_products_add = int(input('Введите кол-во добовляемого товара: '))
for el in range(0, amount_products_add):
    name_product = input('Введите наименование товара: ')
    price_product = int(input('Введите цену товара: '))
    amount_product = int(input('Введите кол-во товара: '))
    product_unit = input('Введите единицу измерения: ')
    temp_tuple = (el + 1, {'название': name_product, 'цена': price_product, 'количество': amount_product,
                           'ед': product_unit})
    products_list.append(temp_tuple)
analytics_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
# for index in range(0, len(products_list)):
#     for characteristic in products_list[index][1]:
#         temp_list = analytics_dict[characteristic]
#         temp_list.append(products_list[index][1].get(characteristic))
#         analytics_dict[characteristic] = temp_list
for characteristic in analytics_dict:
    for index in range(0, len(products_list)):
        analytics_dict[characteristic].append(products_list[index][1][characteristic])
print(analytics_dict)
