import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

f = open("/Users/iseungjin/DB_finalProject/title.basics.tsv","r", encoding='utf-8')
rd = csv.reader(f, delimiter='\t')

sql = "insert into titleBasic(tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMin) " \
      "values (%s,%s,%s,%s,%s,%s,%s,%s)"

data = []
counter = 0

for idx, line in enumerate(rd):
    isAdult = line[4]
    startYear = line[5]
    endYear = line[6]
    runtimeMin = line[7]
    if startYear == "\\N":
        startYear = None
    if endYear == "\\N":
        endYear = None
    if not runtimeMin.isdigit():
        runtimeMin = None
    if isAdult == "\\N":
        isAdult = None
    temp = (line[0], line[1], line[2], line[3], isAdult, startYear, endYear, runtimeMin)
    # if(idx == 771):
    #     print(temp)
    #
    #     break
    data.append(temp)
    counter += 1

    if counter >= 500:
        curs.executemany(sql, data)
        data = []
        counter = 0

curs.executemany(sql, data)
conn.commit()
