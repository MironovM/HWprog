#v.2

def sisend():
    fname = input('Имя файла, пожалуйста: ')
    return fname

def ludemine(fname):
    with open(fname, encoding="utf-8") as f:
        text = f.read()
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace(":", "")
        text = text.replace(";", "")
        text = text.replace("-", "")
        text = text.replace(")", "")
        text = text.replace("“", "")
        text = text.replace('"', "")
        return text

def otsi(text):
    dic = {}
    for word in text:
        if word[-4:] == 'ness':
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    return dic

def arvestama(dic):
    number = 0
    for v in dic.values():
        number += v
    return number

def maksimaalne(dic):
    words = sorted(dic, key = dic.get, reverse = True)
    return words

def tulemus():
    faili = sisend()
    if otsi(ludemine(faili)) == {}:
        print('Нет слов на -ness.')
    else:
        print('Слов на -ness:', arvestama(otsi(ludemine(faili))))
        print('Частотнейшее слово на -ness:', maksimaalne(otsi(ludemine(faili))))

tulemus()
