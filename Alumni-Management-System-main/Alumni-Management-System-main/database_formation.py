#DATABASE AND TABLE FORMATION 

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists alumni_system")
mycursor.execute("use alumni_system")
mycursor.execute("create table if not exists alumni(admission_no int primary key, first_name varchar(20), last_name varchar(20), dob date, gender varchar(20), stream varchar(20), leaving_year int, profession varchar(20), marital_status varchar(20), home_town varchar(20), home_state varchar(20), mob_no bigint, email varchar(50));")
