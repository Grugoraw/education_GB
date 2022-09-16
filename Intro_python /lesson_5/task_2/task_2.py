# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open('text file for task 2.txt', 'r') as text_fail:
    result = [0]
    for line in text_fail:
        result[0] += 1
        check_word = [word for word in line.split()]
        result.append(len(check_word))
print(f'В тексте содержится {result[0]} строк')
for index in range(1, len(result)):
    print(f'Кол-во слов в {index} строке: {result[index]}')
