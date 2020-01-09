
import pymysql

# to check whether database is connected or not
try:
    database=pymysql.connect(host="localhost",user="tanmay",password="localhost12345")
    cursor=database.cursor()

except:
    print("Database is not connected")
    exit

# first will check if database is there or not 
#if not it will create or pass
try:
    create_database="CREATE DATABASE  Login_and_Signup"
    cursor.execute(create_database)
    

except:
    pass

finally:
    database.select_db("Login_and_Signup")
    
try:
    Details='CREATE TABLE details(user_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),email VARCHAR(20),password VARCHAR(20) )'
    cursor.execute(Details)
except:
    pass

try:
    User_info='CREATE TABLE user_info(id INT PRIMARY KEY AUTO_INCREMENT,age INT(3),DOB DATE,image LONGBLOB,about TEXT)'
    cursor.execute(User_info)
except:
    pass
