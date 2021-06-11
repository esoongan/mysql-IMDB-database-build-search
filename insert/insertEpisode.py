import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.episode.tsv", "r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

sql = "insert into episode(tconst, parentTconst, seasonNumber, episodeNumber) values(%s,%s,%s,%s) "


data = []
counter = 0

for line in rd:

    sno = line[2]
    eno = line[3]
    if sno == "\\N":
        sno = None
    if eno == "\\N":
        eno = None
    temp = (line[0], line[1], sno, eno)
    data.append(temp)
    counter += 1

    if counter >= 1300:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
