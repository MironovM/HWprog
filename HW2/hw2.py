#вариант 2
word = input ('Введите слово (кириллицей): ')
a = ""
i = 0
for a in word:
    if i % 2 == 0:
        if a == 'о':
            print (a)
        elif a == 'п':
            print (a)
        elif a == 'е':
            print (a)
    i+=1
