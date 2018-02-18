#v.2
import random

def read_file(fname):
    with open(fname, encoding="utf-8") as f:
        return f.readlines()

def dict(lines):
    d = {}
    for line in lines:
        line = line.split(',')
        d[line[0]] = line[1].split()
    return d

def hint(d):
    word = random.choice(list(d.keys()))
    hint = random.choice(d[word]) + ' '
    for s in word:
        hint += '.'
    return hint

def process():
    print('Загадано слово, являющееся частью легко узнаваемого словосочетания.\nКоличество точек соответствует количеству букв.\nВведите загаданное слово, не используя клавиши Shift и CAPS LOCK.')
    d = dict(read_file('text.csv'))
    word = random.choice(list(d.keys()))
    hint1 = random.choice(d[word])
    hint = hint1 + ' '
    for i in range(len(word)):
        hint += '.'
    print('\n' + hint)
    version = input('Ваша версия: ')
    if word == version:
        print('И это правильный ответ!')
    else:
        version = input('Это неправильный ответ. Попробуйте еще раз: ')
        if word == version:
            print('И это правильный ответ!')
        else:
            version = input('Вы снова не угадали.\nОткройте Google и введите подсказку.\nОтвет на первой же строчке. Итак, ваша версия: ')
            if word == version:
                print('И это правильный ответ!')
            else:
                print('Простите, но нам не о чем с вами разговаривать.')

process()
