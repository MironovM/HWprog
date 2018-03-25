#v.2
import re

with open('Pol_Khofman_-_Levaya_Ruka_Boga.txt', encoding="utf-8") as f:
    text = f.read()
    results_part_1 = re.findall(' нашл[аои]\w+', text)
    results_part_2 = re.findall(' нашел\w+', text)
    results_part_3 = re.findall(' найд\w+', text)
    results_part_4 = re.findall(' нашед\w+', text)
    all_results = results_part_1 + results_part_2 + results_part_3 + results_part_4
    print(all_results)
