# mysql-IMDB-database-build-search

### IMDb Datasets
Subsets of IMDb data are available for access to customers for personal and non-commercial use. You can hold local copies of this data, and it is subject to our terms and conditions. Please refer to the Non-Commercial Licensing and copyright/license and verify compliance.

https://www.imdb.com/interfaces/

## ๐  ํ๋ก์ ํธ ์๊ฐ
๋์ฉ๋์ imdb ๋ฐ์ดํฐ์์ ์ด์ฉํ์ฌ Relationao Database๋ฅผ ๊ตฌ์ถํ๊ณ  ๊ฒ์ํ๋ ํ๋ก๊ทธ๋จ์๋๋ค.
๊ฐ ํ์ผ๋ง๋ค ์ต์ ์ฒ๋ง๊ฐ~์ต๊ฐ์ด์์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ง ๋์ฉ๋ ๋ฐ์ดํฐ๋ฅผ ํจ์จ์ ์ผ๋ก ๊ฒ์ํ๊ธฐ์ํ์ฌ E-R ๋ชจ๋ธ๋ง, ํ์ด๋ธ์ฌ์ค๊ณ, ์ธ๋ฑ์ค๋ฅผ ํ์ฉํ์์ต๋๋ค.

---

## ๐ System Environment

- ์ธ์ด : Python 3.8.4
- DB : 8.0.23 MySQL
- IDE : Pycharm

---

## ์์ธ๋ด์ฉ

### **E-R ๋ชจ๋ธ๋ง**
   - Strong Entity, Weak Entity์ถ์ถ
   - PK์ญํ ์ ํ  ์๋ณ์ ์ถ์ถ

### **ER to RDB**
   - Multivalue attribute๋ฅผ ๋๋ฆฝ์ ์ธ ์ํฐํฐ๋ก ์ฌ์ถ์ถํ์ฌ ์ธ๋ํค๋ก ํ์ด๋ธ ๊ด๊ณ ์ฌ์ค์ 
   - **ERD** 

       <img width="1179" alt="erd" src="https://user-images.githubusercontent.com/68773492/124757868-fd0ccf00-df68-11eb-8d8a-c59abebd4437.png">


### **์ฑ๋ฅ์ต์ ํ**
   - **์๋ธ์ฟผ๋ฆฌ**๋ฅผ ์ฌ์ฉํ์ฌ ๊ฒ์์๋ ํฅ์
       - Dram์ฅ๋ฅด์ ์์๋ฌผ์ ๋ฆฌ๋ทฐ๋ง์์ ๊ฒ์

        ```sql
        **// ๊ธฐ์กด SQL** 

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
        **// ์ฑ๋ฅ์ ํฅ์์ํจ SQL**

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

   - **์ธ๋ฑ์ค**๋ฅผ ์ ์ ํ๊ฒ ์ฌ์ฉํ์ฌ ๊ฒ์์๋๋ฅผ ๋์

        <img width="520" alt="index" src="https://user-images.githubusercontent.com/68773492/124758264-5b39b200-df69-11eb-9e17-bf1bcf906080.png">



