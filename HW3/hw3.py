#вариант 2
word = input ('Введите слово: ')
a = len(word)
d = ''
spisok = list(word)
for i in range(0, a, 1):
    print (d)
    b = i + 1
    d = ''
    for k in range(0, b, 1):
        c = spisok[k]
        d +=c
print (word)
