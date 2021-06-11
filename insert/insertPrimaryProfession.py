import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/name.basics.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql = "insert into primaryProfessions(Pno, Pname) values (%s,%s)"

data = set()
data2 = []
counter = 0

for idx, line in enumerate(rd):
    genre = line[-2]

    if genre == "\\N":
        continue

    elements = genre.split(',')
    for element in elements:
        data.add(element)

data = list(data)
# print(data)

for i in range(len(data)):
    temp = (i, data[i])
    data2.append(temp)

    if i > 10000:
        curs.executemany(sql, data2)
        data2 = []

curs.executemany(sql, data2)
conn.commit()