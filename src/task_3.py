"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
пробелы. Например, если было введено "abc cde def",
то должно быть выведено abcdef """

s = input("Введите предложение: ")
s_new = ''
for i in range(len(s)):
    if s_new.find(s[i]) == -1 and s[i] != ' ':
        s_new += s[i]
print(s_new)