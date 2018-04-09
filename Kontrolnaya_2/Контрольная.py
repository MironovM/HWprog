#v.2

import re

def function_1():
    with open('F.xml', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def function_2(lines):
    dic = {}
    for line in lines:
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1
    return dic

def function_3(dic):
    number = 0
    for v in dic.values():
        number += v
    return number

def function_4():
    sth = function_1()
    with open("Файл_для_записи.txt", "w", encoding="utf-8") as f:
            f.write(str(function_3(function_2(sth))))

function_4()

def function_5():
    with open('F.xml', encoding="utf-8") as f:
        text = f.read
        results = re.findall('<w lemma\w+', text)
    return results

def function_6(results):
    protokeys = re.split('type="', results)
    return protokeys

def function_7(protokeys):
    keys = re.split('">', protokeys)
    return keys

def function_8(keys):
    empty_dict = {}
    for key in keys:
        if
