


# reading from the file and inserting all the records to the database
import pymysql
#step1: connecting to database
db = pymysql.connect(host='localhost',port=3306,user='root',password='india@123',db='realestate')

if db:
    #step2 : create cursor for accessing the records
    cursor = db.cursor()
    #step3: define query
    with open("realestate.csv","r") as fread:
        for line in fread:
            # remove whitespaces
            line = line.strip()
            # split each line 
            output = line.split(",")
            street = output[0]
            city = output[1]
            query = "insert into realestate values('{}','{}')".format(street,city)
            cursor.execute(query)

db.commit()
db.close()
            
