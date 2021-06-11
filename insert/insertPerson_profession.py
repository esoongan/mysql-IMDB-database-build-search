import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/name.basics.tsv", "r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

# 임시테이블에 삽입
sql = "insert into person_job_temp(nconst, Pname) values(%s, %s)"

# 참조무결성을 만족하도록 테이블 재삽입
sql2 = "insert into person_primaryProfessions(nconst, Pno) select b.nconst, a.Pno from primaryProfessions a, person_job_temp b where a.Pname = b.Pname"
curs.execute(sql2)
conn.commit()

data = []
counter = 0

for line in rd:

    tconst = line[0]
    PnameList = line[-2].split(',')

    for Pname in PnameList:
        temp = (tconst, Pname)
        data.append(temp)
        counter+=1

    if counter >= 10000:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
