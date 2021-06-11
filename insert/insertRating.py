import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.ratings.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

tconst = ""
sql = "insert into ratings(Rid, tconst, averageRating, numVotes) values (%s, %s,%s)"

data = []
counter = 0

for line in rd:

    temp = (line[0], line[1], line[2])
    data.append(temp)
    counter += 1

    if counter >= 1300:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
