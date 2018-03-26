#v.2
import re

def function1():
    with open('Pol_Khofman_-_Levaya_Ruka_Boga.txt', encoding="utf-8") as f:
        text = f.read()
        results_part_1 = re.findall(' нашл[аио]\w+', text)
        results_part_2 = re.findall(' нашел\w+', text)
        results_part_3 = re.findall(' найд\w+', text)
        results_part_4 = re.findall(' нашед\w+', text)
        all_results = results_part_1 + results_part_2 + results_part_3 + results_part_4
    return all_results
def function2(all_results):
    dic = {}
    for word in all_results:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic
def function3():
    sth = function1()
    print(function2(sth))

function3()
