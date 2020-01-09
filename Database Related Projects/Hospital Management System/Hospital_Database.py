
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
    create_database="CREATE DATABASE  hospital_management_system"
    cursor.execute(create_database)
    

except:
    pass

finally:
    database.select_db("hospital_management_system")
    
    

#table for patient
try:
    create_patient_table="CREATE TABLE  patient(p_id INT PRIMARY KEY AUTO_INCREMENT,p_name CHAR(30),p_address VARCHAR(50),p_diagnosis VARCHAR(20))"
    cursor.execute(create_patient_table)

except :
    pass


#table for hospital
try:
    create_hospital_table="CREATE TABLE  hospital(H_id INT PRIMARY KEY AUTO_INCREMENT,H_name CHAR(30),H_address VARCHAR(50),H_city VARCHAR(20))"
    cursor.execute(create_hospital_table)

except  :
    pass

#table for medical
try:
    create_medical_table="CREATE TABLE  medical(record_id INT PRIMARY KEY AUTO_INCREMENT,Date_of_examination DATE,Problem VARCHAR(50))"
    cursor.execute(create_medical_table)

except  :
    pass

#table for Doctor
try:
    create_doctor_table="CREATE TABLE  doctor(doctor_id INT PRIMARY KEY AUTO_INCREMENT,D_name CHAR(20),qualification VARCHAR(20),salary INT)"
    cursor.execute(create_doctor_table)

except:
    pass

# table for parking
try:
    create_medical_table="CREATE TABLE  parking( parking_id INT PRIMARY KEY AUTO_INCREMENT,vehicle_no VARCHAR(10))"
    cursor.execute(create_medical_table)

except:
    pass

