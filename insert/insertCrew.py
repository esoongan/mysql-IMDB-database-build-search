import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.crew.tsv","r", encoding='utf-8')

rd = csv.reader(f, delimiter='\t')

#외래키를 설정하지 않은 temp테이블
sql1 = "insert into directors_temp(tconst, nconst) values(%s, %s)"
# temp테이블에서 외래키 참조무결성을 위해 nameBasic에 없는 nconst를 삭제
sql2 = "delete from directors_temp where nconst not in select nconst from nameBasic"
# 외래키가 설정된 directors테이블에 데이터 삽입
sql3 = "insert into directors(tconst, nconst) select tconst, nconst from directors_temp"


sql4 = "insert into writers_temp(tconst, nconst) values(%s, %s)"
sql5 = "delete from writers_temp where nconst not in (select nconst from nameBasic)"
sql6 = "insert into writers(tconst, nconst) select tconst, nconst from writers_temp"

curs.execute(sql6)
conn.commit()

# data = []
# counter = 0
#
# for line in rd:
#     tconst = line[0]
#     writers = line[2].split(',')
#
#     for writer in writers:
#         if writer == '\\N':
#             continue
#         temp = (tconst, writer)
#         data.append(temp)
#         counter +=1
#
#     if counter >= 10000:
#         curs.executemany(sql4, data)
#         data = []
#         counter = 0
#
# curs.executemany(sql4, data)
# conn.commit()

# for line in rd:
#     tconst = line[0]
#     directors = line[1].split(',')
#
#     for director in directors:
#         if director == '\\N' or director[:2] !='nm':
#             continue
#         temp = (tconst, director)
#         data.append(temp)
#         counter +=1
#
#     if counter >= 1300:
#         curs.executemany(sql, data)
#         data = []
#         counter = 0
#
# curs.executemany(sql, data)
# conn.commit()
