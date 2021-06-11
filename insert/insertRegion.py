import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.akas.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

def insert_region():
    sql = "insert into title_region_temp(tconst, region) values (%s,%s)"

    data = set()
    counter = 0

    for line in rd:
        region = line[3]

        if region == "\\N":
            continue

        temp = (line[0], region)
        data.add(temp)
        counter += 1

        if counter >= 30000:
            curs.executemany(sql, list(data))
            data = set()
            counter = 0

    curs.executemany(sql, list(data))
    conn.commit()

insert_region()
