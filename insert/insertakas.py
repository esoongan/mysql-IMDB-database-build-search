import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.akas.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql1 = "insert into movie_title(Tid, tconst, title) values (%s, %s, %s)"
sql2 = "insert into movie_region(Rid, tconst, region) values (%s, %s, %s)"
sql3 = "insert into movie_language(Lid, tconst, language) values (%s, %s, %s)"

data = []
counter = 0

for idx, line in enumerate(rd):
    tconst = line[0]
    lan = line[4]
    if lan == "\\N":
        continue

    temp = (counter, tconst, lan)
    data.append(temp)
    counter += 1

    if counter >= 2000:
        curs.executemany(sql3, data)
        conn.commit()
        break


