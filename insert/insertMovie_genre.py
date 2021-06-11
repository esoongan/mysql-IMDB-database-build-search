import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.basics.tsv", "r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql2 = "insert into movie_genre(tconst, Gno) select b.tconst, a.Gno from genre a, movie_genre_temp b where a.Gname = b.Gname"
# curs.execute(sql)
# conn.commit()

data = []
counter = 0

for line in rd:

    tconst = line[0]
    GnameList = line[-1].split(',')

    for Gname in GnameList:
        temp = (tconst, Gname)
        data.append(temp)
        counter+=1

    if counter >= 1300:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
