import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

# f = open("/Users/iseungjin/DB_finalProject/title.ratings.tsv","r", encoding='utf-8')
#
# rd = csv.reader(f, delimiter='\t')

sql = 'insert into title_episode(tconst, parentTconst, seasonNumber, episodeNumber) select e.tconst, e.parentTconst, e.seasonNumber, e.episodeNumber from episode e where e.tconst in (select tconst from titleBasic) and e.parentTconst in (select tconst from titleBasic) '
curs.execute(sql)
conn.commit()
#
# data = []
# counter = 0
#
# for line in rd:
#     tconst = line[0]
#
#     temp = (line[1], line[2], tconst)
#     data.append(temp)
#     counter += 1
#
#     if counter >= 1300:
#         curs.executemany(sql, data)
#         data = []
#         counter = 0
#
# curs.executemany(sql, data)
# conn.commit()
#
