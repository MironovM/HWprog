#v.2
import re
import os

def function1():
    start_path = "."
    for dirs in os.walk(start_path):
        res1 = dirs
    return res1

def function2(res1):
    res2 = re.findall(res1, '[а-я]')
    return res2

def function3(res2):
    dic = {}
    for res3 in res2:
        if res3 in dic:
            dic[res3] += 1
        else:
            dic[res3] = 1
    return dic

def function4():
    sth = function1()
    print(function3(function2(sth)))

function4()
