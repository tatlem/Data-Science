# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

words_input = input('Input sentence: ')
words = words_input.split()
row_num = 1

for word in words:
    print("{:<3} {:10}".format(row_num, word[0:10]))
    row_num += 1