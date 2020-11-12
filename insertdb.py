import pymysql
#step1: connecting to database
db = pymysql.connect(host='localhost',port=3306,user='root',password='india@123',db='realestate')

if db:
    #step2 : create cursor for accessing the records
    cursor = db.cursor()
    #step3: define query
    query = "insert into realestate values('{}','{}')".format("BanjaraHills","Hyderabad")
    #step4: execute
    cursor.execute(query)
    print(cursor.rowcount, " record inserted")
db.commit()
db.close()