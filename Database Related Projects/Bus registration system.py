import  pymysql


def insert_passenger_data():
    insert_data ="INSERT INTO passenger VALUES('ABCD','Panvel')"
    cursor.execute(insert_data)
    database.commit()
try:    
    database= pymysql.connect(host="localhost",user="tanmay",password="localhost12345")
    cursor=database.cursor()
    database.select_db("Bus_reservation_system")
    x=1
except:
    print('Error')
    x=0
finally:
    insert_passenger_data()
    cursor.execute("SHOW TABLES")
    cursor.execute("SELECT * FROM passenger")
    for databases in cursor:
         print(databases)



