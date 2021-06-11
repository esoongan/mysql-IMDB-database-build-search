import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/name.basics.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql = "insert into nameBasic(nconst, primaryName, birthYear, deathYear) values (%s,%s,%s,%s)"

data = []
counter = 0

for line in rd:
    birthYear = line[2]
    deathYear = line[3]
    if line[2] == "\\N":
        birthYear = None
    if line[3] == "\\N":
        deathYear = None
    temp = (line[0], line[1], birthYear, deathYear)
    data.append(temp)
    counter += 1

    if counter >= 1300:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
