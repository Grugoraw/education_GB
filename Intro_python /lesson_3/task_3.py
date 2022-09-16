# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(val_1, val_2, val_3):
    if val_1 <= val_2 and val_1 <= val_3:
        return val_2 + val_3
    elif val_2 <= val_3 and val_2 <= val_1:
        return val_1 + val_3
    else:
        return val_1 + val_2
