import time
import tablib
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                           user='db2020',
                           password='db2020',
                           db='imdb')

curs = conn.cursor(pymysql.cursors.DictCursor)

def 제목으로_영화검색():
    sql = 'select * from movie where primaryTitle = %s'
    data = []
    print("영화제목을 입력하세요: ")
    title = input().strip()
    start_time = time.time()

    curs.execute(sql, title)
    row = curs.fetchone()
    elapsed_time = time.time() - start_time

    data.append((row['tconst'],row['titleType'],row['primaryTitle'],row['originalTitle'],row['isAdult'],row['startYear'],row['endYear'],row['runtimeMin']))
    headers = ['영화번호', '타입', '제목', '원본제목', '성인물', '개봉일', '종료일', '런타임']
    data = tablib.Dataset(*data, headers=headers)

    print(data)
    print("반응시간 : %f" %elapsed_time)

def 특정_배우가_출연하는_영화_별점_높은순():
    sql = 'select movie.*, review.averageRating from movie, review where movie.tconst = review.tconst and movie.tconst in (select tconst from principals_temp where nconst in (select nconst from person where primaryName = %s) and category = "actor") order by review.averageRating desc'
    data = []

    print("배우 이름을 입력하세요: ")
    act_name = input().strip()
    start_time = time.time()

    curs.execute(sql, act_name)
    row = curs.fetchone()
    while (row):
        data.append((row['tconst'], row['titleType'], row['primaryTitle'], row['originalTitle'], row['isAdult'], row['startYear'], row['endYear'], row['runtimeMin'], row['averageRating']))

        row = curs.fetchone()
    elapsed_time = time.time() - start_time

    headers = ['영화번호', '타입', '제목', '원본제목', '성인물', '개봉일', '종료일', '런타임', '별점']
    data = tablib.Dataset(*data, headers=headers)

    print(data)
    print("반응시간 : %f" % elapsed_time)

def 특정_감독이_제작한_영화_개봉연도_최근순():
    sql = 'select * from movie where movie.tconst in (select tconst from principals_temp where nconst in (select nconst from person where primaryName = %s) and category = "director") order by review.averageRating desc'
    sql2 = 'select * from movie where tconst in (select tconst from directors where nconst = (select nconst from person where primaryName = %s)) order by startYear desc'
    data = []
    print("감독 이름을 입력하세요: ")
    director_name = input().strip()

    start_time = time.time()

    curs.execute(sql2, director_name)
    row = curs.fetchone()
    while (row):
        data.append((row['tconst'], row['titleType'], row['primaryTitle'], row['originalTitle'], row['isAdult'], row['startYear'], row['endYear'], row['runtimeMin']))
        row = curs.fetchone()

    elapsed_time = time.time() - start_time

    headers = ['영화번호', '타입', '제목', '원본제목', '성인물', '개봉일', '종료일', '런타임']

    data = tablib.Dataset(*data, headers=headers)
    print(data)
    print("반응시간 : %f" % elapsed_time)


def drama_장르_리뷰많은순():
    sql = 'select d.*, c.numVotes from (select b.tconst, b.numVotes from (select tconst from movie_genre where Gno = (select Gno from genre where Gname="Drama")) a, review b where a.tconst=b.tconst order by b.numVotes desc) c , movie d where c.tconst = d.tconst limit 50'

    data = []
    start_time = time.time()

    curs.execute(sql)
    row = curs.fetchone()
    while (row):
        data.append((row['tconst'], row['titleType'], row['primaryTitle'], row['originalTitle'], row['isAdult'],row['startYear'], row['endYear'], row['runtimeMin'], row['numVotes']))
        row = curs.fetchone()

    elapsed_time = time.time() - start_time

    all_row = len(data)
    data = data[:100]
    headers = ['영화번호', '타입', '제목', '원본제목', '성인물', '개봉일', '종료일', '런타임', '리뷰수']

    data = tablib.Dataset(*data, headers=headers)
    print(data)
    print("반응시간 : %f" % elapsed_time)
    print("총 row수 :", all_row)

def drama_장르_별점높은순():
    sql = 'select d.*, c.averageRating from (select b.tconst, b.averageRating from (select tconst from movie_genre where Gno = (select Gno from genre where Gname="Drama")) a, review b where a.tconst=b.tconst order by b.averageRating desc) c , movie d where c.tconst = d.tconst'

    data = []
    start_time = time.time()

    curs.execute(sql)
    row = curs.fetchone()
    while (row):
        data.append((row['tconst'], row['titleType'], row['primaryTitle'], row['originalTitle'], row['isAdult'], row['startYear'], row['endYear'], row['runtimeMin'], row['averageRating']))
        row = curs.fetchone()

    elapsed_time = time.time() - start_time

    all_row = len(data)
    data = data[:100]
    headers = ['영화번호', '타입', '제목', '원본제목', '성인물', '개봉일', '종료일', '런타임', '별점']
    data = tablib.Dataset(*data, headers=headers, )
    print(data)
    print("반응시간 : %f" % elapsed_time)
    print("총 row수 : ", all_row)

def 에피소드가_5000편이상인_시리즈물_에피소드많은순():
    print("에피소드가 5000편 이상인 시리즈물 정보를 출력합니다.")
    print("----------------------------------------")
    data = []

    sql = 'select e.*, p.episodeNo from movie e, (select parentTconst, count(*) as episodeNo from episode group by parentTconst having count(parentTconst)>5000) p where p.parentTconst = e.tconst order by episodeNo desc'
    start_time = time.time()

    curs.execute(sql)
    row = curs.fetchone()
    while (row):
        data.append((row['tconst'],
                         row['titleType'],
                         row['primaryTitle'],
                         row['isAdult'],
                         row['startYear'],
                         row['endYear'],
                         row['runtimeMin'],
                         row['episodeNo']))


        row = curs.fetchone()
    elapsed_time = time.time() - start_time

    headers = ('tconst',
               'titleType',
               'Title',
               'isAdult',
               'startYear',
               'endYear',
               'runtimeMin',
               'episodeNo')

    data = tablib.Dataset(*data, headers=headers)
    print(data)
    print("반응시간 : %f" % elapsed_time)



def 직업이작곡가이면서감독인사람의정보_나이적은순():
    print("직업이 작곡가이면서 감독인 사람의 정보를 출력합니다.")
    print("----------------------------------------")
    data = []
    sql = 'select * from person where nconst in (select a.nconst from (select nconst from person_primaryProfessions where Pno = (select Pno from primaryProfessions where Pname="composer")) a,(select nconst from person_primaryProfessions where Pno = (select Pno from primaryProfessions where Pname="director")) b where a.nconst = b.nconst) order by birthYear desc'
    start_time = time.time()

    curs.execute(sql)

    row = curs.fetchone()
    while (row):
        data.append((row['nconst'],
                         row['primaryName'],
                         row['birthYear'],
                         row['deathYear']))


        row = curs.fetchone()

    all_row = len(data)
    elapsed_time = time.time() - start_time

    headers = ('nconst',
               'name',
               'birth',
               'death')

    data = tablib.Dataset(*data, headers=headers)
    print(data)
    print("반응시간 : %f" % elapsed_time)
    print("총 row수 : ", all_row)


def 오천편이상의작품을집필한_작가의정보_작품많은순():
    print("오천편이상의작품을집필한_작가의정보를 출력합니다.")
    print("----------------------------------------")
    data = []

    sql = 'select a.total, b.* from (select nconst, count(nconst) as total from writers group by nconst having count(*)>5000) a, person b where a.nconst=b.nconst order by total desc'
    start_time = time.time()

    curs.execute(sql)

    row = curs.fetchone()
    while (row):
        data.append((row['nconst'],
                         row['primaryName'],
                         row['birthYear'],
                         row['deathYear'],
                         row['total']))


        row = curs.fetchone()
    elapsed_time = time.time() - start_time

    headers = ('nconst',
               'name',
               'birth',
               'death',
               '총집필작품수')

    data = tablib.Dataset(*data, headers=headers)
    print(data)
    print("반응시간 : %f" % elapsed_time)

if __name__ == '__main__':
    while(True):
        print("==============================================")
        print("1번 : 제목으로 영화검색")
        print("2번 : 특정 배우가 등장하는 영화를 별점이 높은순으로 검색")
        print("3번 : 특정감독이 제작한 영화를 개봉연도가 빠른순으로 검색")
        print("4번 : drama장르의 영화를 리뷰가 많은순으로 검색")
        print("5번 : drama장르의 영화를 별점이 높은순으로 검색")
        print("==============================================")
        print("6번 : 에피소드가 5000편 이상인 시리즈물을 에피소드가 많은순으로 검색")
        print("7번 : 직업이 작곡가이면서 감독인 사람의 정보를 나이가 적은순으로 검색")
        print("8번 : 5000편이상의 작품을 집필한 작가정보를 작품이 많은순으로 검색")
        print("9번 : 검색을 종료합니다.")

        menu = int(input())


        if(menu == 1):
            제목으로_영화검색()
        elif(menu == 2):
            특정_배우가_출연하는_영화_별점_높은순()
        elif (menu == 3):
            특정_감독이_제작한_영화_개봉연도_최근순()
        elif(menu == 4):
            drama_장르_리뷰많은순()
        elif (menu == 5):
            drama_장르_별점높은순()
        elif(menu == 6):
            에피소드가_5000편이상인_시리즈물_에피소드많은순()
        elif (menu == 7):
            직업이작곡가이면서감독인사람의정보_나이적은순()
        elif(menu == 8):
            오천편이상의작품을집필한_작가의정보_작품많은순()
        elif(menu ==9):
            break
        else:
            print("번호를 잘못입력하였습니다.")

