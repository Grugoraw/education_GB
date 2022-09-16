# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(user_str: str):
    return user_str.capitalize()


def all_cap(user_str: str):
    word_list = user_str.split()
    for index in range(0, len(word_list)):
        word_list[index] = int_func(word_list[index])
    return ' '.join(word for word in word_list)


print(int_func('text'))
print(all_cap('text text text text text text'))

