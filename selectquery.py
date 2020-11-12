

import pymysql
#step1: connecting to database
db = pymysql.connect(host='localhost',port=3306,user='root',password='india@123',db='realestate')

if db:
    #step2 : create cursor for accessing the records
    cursor = db.cursor()
    query = "select * from realestate"
    cursor.execute(query)
    for record in cursor.fetchall():
        print(record[0])
        print(record[1])
        print("----------")

db.close()
    
    