import pymysql

try:
    database=pymysql.connect(host="localhost",user="tanmay",password="localhost12345")
    cursor=database.cursor()

except:
    print("Database is not connected")
    exit

create_database="CREATE DATABASE IF NOT EXISTS hotel_management_system"
cursor.execute(create_database)

database.select_db("hotel_management_system")

Hotel="CREATE TABLE IF NOT EXISTS Hotel(Hotel_Id INT PRIMARY KEY AUTO_INCREMENT,Hotel_Name VARCHAR(20),Star_rate INT(5))"
cursor.execute(Hotel)

Rooms="CREATE TABLE IF NOT EXISTS Rooms(Room_Type VARCHAR(10),Room_No VARCHAR(10))"
cursor.execute(Rooms)

Location="CREATE TABLE IF NOT EXISTS Hotel_Location(Town VARCHAR(10),Street VARCHAR(10),Pincode INT)"
cursor.execute(Location)

Cost="CREATE TABLE IF NOT EXISTS Cost(Hotel_Name VARCHAR(20),Amount INT)"
cursor.execute(Cost)