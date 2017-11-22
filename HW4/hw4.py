#вариант 2 
with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    lines = text.splitlines()
    mn = len(lines[0])
    mx = len(lines[0])
    for line in lines:
        if len(line) > mx:
            mx = len(line)
        if len(line) < mn:
            mn = len(line)
if mn == 0:
    print('На ноль делить нельзя!')
else:
    print(mx/mn)
