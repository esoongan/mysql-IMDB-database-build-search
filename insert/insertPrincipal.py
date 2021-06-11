import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.principals.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql = "insert into principals_temp(tconst, ordering, nconst, category) values (%s, %s,%s,%s)"

data = []
counter = 0
ex = 0
for idx, line in enumerate(rd):
    if idx == 0:
        continue
    # tconst = line[0]
    # ordering = line[1]
    # nconst = line[2]
    # category = line[3]

    temp = (line[0], line[1], line[2], line[3])
    data.append(temp)
    counter += 1

    if counter >= 10000:
        curs.executemany(sql, data)
        data = []
        counter = 0
        ex += 1

    if ex == 1000:
        curs.executemany(sql, data)
        conn.commit()
        break
