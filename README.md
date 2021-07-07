# mysql-IMDB-database-build-search

### IMDb Datasets
Subsets of IMDb data are available for access to customers for personal and non-commercial use. You can hold local copies of this data, and it is subject to our terms and conditions. Please refer to the Non-Commercial Licensing and copyright/license and verify compliance.

https://www.imdb.com/interfaces/

## 📌  프로젝트 소개
대용량의 imdb 데이터셋을 이용하여 Relationao Database를 구축하고 검색하는 프로그램입니다.
각 파일마다 최소 천만개~억개이상의 데이터를 가진 대용량 데이터를 효율적으로 검색하기위하여 E-R 모델링, 테이블재설계, 인덱스를 활용하였습니다.

---

## 📌 System Environment

- 언어 : Python 3.8.4
- DB : 8.0.23 MySQL
- IDE : Pycharm

---

## 상세내용

### **E-R 모델링**
   - Strong Entity, Weak Entity추출
   - PK역할을 할 식별자 추출

### **ER to RDB**
   - Multivalue attribute를 독립적인 엔티티로 재추출하여 외래키로 테이블 관계 재설정
   - **ERD** 

       <img width="1179" alt="erd" src="https://user-images.githubusercontent.com/68773492/124757868-fd0ccf00-df68-11eb-8d8a-c59abebd4437.png">


### **성능최적화**
   - **서브쿼리**를 사용하여 검색속도 향상
       - Dram장르의 영상물을 리뷰많은순 검색

        ```sql
        **// 기존 SQL** 

        SELECT   m.*,
                 r.numvotes
        FROM     movie m,
                 review r
        WHERE    m.tconst IN
                 (
                        SELECT tconst
                        FROM   movie_genre w here gno =
                               (
                                      SELECT gno
                                      FROM   genre
                                      WHERE  gname="Drama"))
        AND      m.tconst = r.tconst
        ORDER BY r.numvotes des c
        ```

        ```sql
        **// 성능을 향상시킨 SQL**

        SELECT d.*,
               c.numvotes
        FROM   (
                        SELECT   b.tconst,
                                 b.numvotes
                        FROM     (
                                        SELECT tconst
                                        FROM   movie_genre
                                        WHERE  gno =
                                               (
                                                      SELECT gno
                                                      FROM   genre
                                                      WHERE  gname="Drama")) a,
                                 review b
                        WHERE    a.tconst=b.tcons t
                        ORDER BY b.numvotes DESC) c ,
               movie d
        WHERE  c.tconst = d.tconst
        ```

   - **인덱스**를 적절하게 사용하여 검색속도를 높임

        <img width="520" alt="index" src="https://user-images.githubusercontent.com/68773492/124758264-5b39b200-df69-11eb-9e17-bf1bcf906080.png">



