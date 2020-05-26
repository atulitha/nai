import codecs
import csv
with codecs.open('data.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    #rows = [row for row in reader]
    for row in reader:
        ip,username,password=[row[0],row[1],row[2]]
        print (ip,username,password)
