# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# 1 Способ
# result_list = []
# with open('text file for task 4.txt', 'r') as user_text:
#     for line in user_text:
#         temp_list = [el for el in line.split()]
#         temp_list[0] = translate_dict.get(temp_list[0])
#         result_list.append(' '.join(w for w in temp_list))
# with open('new text file for task 4.txt', 'w') as result_text:
#     for line in range(len(result_list)):
#         result_text.write(result_list[line] + '\n')

# 2 Способ
with open('text file for task 4.txt', 'r') as user_text:
    for line in user_text:
        temp_list = [el for el in line.split()]
        temp_list[0] = translate_dict.get(temp_list[0])
        with open('new text file for task 4.txt', 'a+') as result_text:
            result_text.write(' '.join(w for w in temp_list) + '\n')
