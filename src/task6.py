"""Слова"""
"""Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько
различных слов содержится в этом тексте"""

a = []
b = 'Уж близок полдень, жар пылает как пахарь битва отдыхает, кой-где битва'
for i in b.split():
    a += i.split()
print(len(set(a)))
# print(b.split())