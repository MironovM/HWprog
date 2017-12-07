#вариант 1
with open("quotes.txt", encoding="utf-8") as f:
    for line in f:
        spisok = line.split()
        if spisok[2]=='—' or spisok[3]=='—' or spisok[4]=='—' or spisok[5]=='—' or spisok[6]=='—' or spisok[7]=='—' or spisok[8]=='—' or spisok[9]=='—' or spisok[10]=='—' or spisok[11]=='—' and len(spisok[1])<5:
            print (line)

