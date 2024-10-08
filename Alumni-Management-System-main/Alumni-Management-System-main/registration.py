#Module of Registrtion Option

import mysql.connector

def register():
    try:
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        mycursor=mycon.cursor()

        print()
        print(" ~~~Registration Menu~~~ ")
        print(" ===================================")
        print(" Please enter the following details.")
        print()
    
        admission_no=int(input("Admission Number: "))
        first_name=input("First Name: ")
        last_name=input("Last Name: ")
        dob=input("DOB(YYYY-MM-DD): ")
        gender=input("Gender(M/F): ")
        stream=input("Stream: ")
        leaving_year=int(input("Year Of Leaving(yyyy): "))
        profession=input("Profession: ")
        marital_status=input("Marital Status (Married/Unmarried): ")
        home_town=input("Home town: ")
        home_state=input("Home State: ")
        mob_no=int(input("Mobile Number: "))
        email=input("E-Mail: ")

        st= "insert into alumni values({}, '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', {}, '{}')".format(admission_no, first_name, last_name, dob, gender, stream, leaving_year, profession, marital_status, home_town, home_state, mob_no, email)
        mycursor.execute(st)
        mycon.commit()
        
        print()
        print("Record inserted!")
        

    except:
        if mysql.connector.errors.IntegrityError:
            print()
            print("================================================================")
            print("This Admission Number already exist.")
            
        else:
            print("Something went wrong...!!! Please try again...!!!")
            



    print("================================================================")
    ch=input("Enter 1 to insert another record or 2  to return back to Main menu: ")
    if ch=='1':
        register()

