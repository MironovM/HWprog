import random

def FNom():
    with open("1Nom.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def FAbl():
    with open("1Abl.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def FAcc():
    with open("1Acc.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def FVerb():
    with open("1Verb.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def SNom():
    with open("2Nom.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def SAdv():
    with open("2Adv.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def SVerb():
    with open("2Verb.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def SAbl():
    with open("2Abl.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def TF():
    with open("TF.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def TNom():
    with open("3Nom.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def TVerb():
    with open("3Verb.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def TAdv():
    with open("3Adv.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def punct():
    with open("punct.txt", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return random.choice(words)

def line1():
    return FNom() + ' ' + FAbl() + ' ' + FAcc() + ' ' + FVerb() + punct()

def line2():
    return SNom() + ' ' + SAdv() + ' ' + SVerb() + ' ' + SAbl() + punct()

def line3():
    return TF() + ' ' + TNom() + ' ' + TVerb() + ' ' + TAdv() + punct()

def make_line():
    line = random.choice([1,2,3])
    if line == 1:
        return line1()
    elif line == 2:
        return line2()
    else:
        return line3()

for n in range(4):
    print(make_line())
