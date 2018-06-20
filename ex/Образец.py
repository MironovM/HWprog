import csv
import re

def f1():
    with open('_itartass1.xhtml', encoding="windows-1251") as f:
        text = f.read()
        res1 = re.search('''=".+" name="docid"''')
        res2 = re.search('''>.+</title>''')
        res3 = re.search('''=".+" name="author"''')
        res4 = re.search('''=".+" name="created"''')
        res5 = re.search('''=".+" name="topic"''')
        res6 = re.search('''"=.+" name="tagging"''')
        rez1 = re.sub(r,'', '="', res1)
        rez12 = re.sub(r,'', '" name="docid"', rez1)
        rez2 = re.sub(r,'', '>', res2)
        rez22 = re.sub(r,'', '</title>', rez2)
        rez3 = re.sub(r,'', '="', res3)
        rez32 = re.sub(r,'', '" name="author"', rez3)
        rez4 = re.sub(r,'', '="', res4)
        rez42 = re.sub(r,'', '" name="created"', rez4)
        rez5 = re.sub(r,'', '="', res5)
        rez52 = re.sub(r,'', '" name="topic"', rez5)
        rez6 = re.sub(r,'', '="', res6)
        rez62 = re.sub(r,'', '" name="tagging"', rez6)
        result1 = rez12 + ',' + rez22 + ',' + rez32 + ',' + rez42 + ',' + rez52 + ',' + rez62
    return result1

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
 
if __name__ == "__main__":
    
    data = ["doc_id,title,author,created,topic,tagging".split(","),
            result1.split(",")
            ]
    
    path = "file.csv"
    csv_writer(data, path)
