#v.2
import re

def f1():
    with open('1.html', encoding="utf-8") as f:
        text = f.read()
    lin = text.splitlines()
    results = re.match(r'<p><span class="no-wikidata" data-wikidata-property-id="P421">', lin)
    print(results)

#def function_2(results):
#    rezalty = re.split(r'>', results)
#    return rezalty

#def function_3(rezalty):
#    if rezalty[3:] == 'UTC':
#        print(rezalty)
#    dic = {}
    #for waist in rezulty:
#    if rezalty[3:] == 'UTC':
#        if rezalty in dic:
#            dic[rezalty] += 1
#        else:
#            dic[rezalty] = 1
#    return dic

#def function_4():
#    fal = function_1()
#    print(function_3(function_2(fal)))

f1()
