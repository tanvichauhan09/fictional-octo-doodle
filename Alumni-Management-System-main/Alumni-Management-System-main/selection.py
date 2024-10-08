#module of all selection function given in program

import mysql.connector


def select_record(): #specific record function
    
    print("\n ~~~SELECT MENU~~~")
    print("=======================================")

    try:
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        mycursor=mycon.cursor()

            
        
        print("To Select, Enter following numbers. ")
        print()
        

        print("1.Admission Number")
        print("2.First Name")
        print("3.Last Name")
        print("4.DOB")
        print("5.Gender")
        print("6.Stream")
        print("7.Leaving Year")
        print("8.Profession")
        print("9.Marital Status")
        print("10.Home Town")
        print("11.Home State")
        print("12.Mobile Number")
        print("13.E-Mail")
        print()

        column=input("Enter your choosen number: ")
        print()

        if column=='1':
            adm=int(input("Enter the Admission Number: "))
            sr="select * from alumni where admission_no='%s' " %(adm)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()

        elif column=='2':
            F_name=str(input("Enter the First Name: "))
            sr=" select * from alumni where first_name='%s' "%(F_name)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        elif column=='3':
            L_name=str(input("Enter Last Name: "))
            sr=" select * from alumni where last_name='%s' "%(L_name)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        elif column=='4':
            dob=str(input("Enter DOB (YYYY-MM-DD): "))
            sr=" select * from alumni where dob='%s' "%(dob)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        



        elif column=='5':
            gender=str(input("Enter Gender (M/F): "))
            sr=" select * from alumni where gender='%s' "%(gender)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        


        elif column=='6':
            stream=str(input("Enter Stream: "))
            sr=" select * from alumni where stream='%s' "%(stream)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        



        elif column=='7':
            l_year=int(input("Enter Leaving Year (YYYY): "))
            sr=" select * from alumni where leaving_year='%d' "%(l_year)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        
        
        elif column=='8':
            profession=str(input("Enter profession: "))
            sr=" select * from alumni where profession='%s' "%(profession)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        



        elif column=='9':
            marital=str(input("Enter Marital Status: "))
            sr=" select * from alumni where marital_status='%s' "%(marital)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        


        elif column=='10':
            h_town=str(input("Enter Home Town: "))
            sr=" select * from alumni where home_town='%s' "%(h_town)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



        
        
                    
        elif column=='11':
            h_state=str(input("Enter Home state: "))
            sr=" select * from alumni where home_state='%s' "%(h_state)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



                        
        

        elif column=='12':
            mob_no=int(input("Enter Mobile Number: "))
            sr=" select * from alumni where mob_no='%d' "%(mob_no)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



                        


        elif column=='13':
            email=str(input("Enter Email: "))
            sr=" select * from alumni where email='%s' "%(email)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()



                        
        else:
            print("Invalid Choice, Please Try Again...")
            select_record()
        

    except:
         print("Something went wrong...!!! Please try again...!!!")
         select_record()

    
    print("================================================================")
    ch=input("Enter 1 to select records again or 2  to return back to Main menu: ")
    if ch=='1':
        select_record()





def select_range(): #range select function
    try:
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        mycursor=mycon.cursor()

        
        print("\n~~~SELECT BY RANGE~~~ ")
        print("====================================")
            
        
        print("To Select, Press following numbers. ")

        print("1. Admission Number")
        print("2. DOB")
        print("3. Leaving Year")
        column=input("Enter your choosen number: ")
        print()

        if column=='1':
            e1=int(input("From Admission Number: "))
            e2=int(input("To Admission Number: "))
            print()
            sr=" select * from alumni where admission_no >= '%d' and admission_no <= '%d' "%(e1,e2)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()


        elif column=='2':
            e1=str(input("From DOB: "))
            e2=str(input("To DOB: "))
            print()
            sr=" select * from alumni where dob >= '%s' and dob <= '%s' "%(e1,e2)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()

        elif column=='3':
            e1=int(input("From Leaving Year: "))
            e2=int(input("To Leaving Year: "))
            print()
            sr=" select * from alumni where leaving_year >= '%d' and leaving_year <= '%d' "%(e1,e2)
            mycursor.execute(sr)
            data=mycursor.fetchall()
            for i in data:
                admission_no=  i[0] 
                first_name=    i[1]
                last_name=     i[2]
                dob=           i[3]
                gender=        i[4]                  
                stream=        i[5]
                leaving_year=  i[6]
                profession=    i[7]
                marital_status=i[8]
                home_town=     i[9]
                home_state=    i[10]
                mob_no=        i[11]
                email=         i[12]

                print(" Admission No        : %d" %(admission_no))
                print(" First Name          : %s" %(first_name))
                print(" Last Name           : %s" %(last_name))
                print(" DOB(YYYY-MM-DD)     : %s" %(dob))
                print(" Gender(M/F)         : %s" %(gender))
                print(" Stream              : %s" %(stream))
                print(" Leaving Year        : %d" %(leaving_year))
                print(" Profession          : %s" %(profession))
                print(" Marital Status(M/UM): %s" %(marital_status))
                print(" Home Town           : %s" %(home_town))
                print(" Home State          : %s" %(home_state))
                print(" Mobile No           : %d" %(mob_no))
                print(" E-Mail              : %s" %(email))
                print()

        else:
            select_range()

    except:
        print("Something went wrong...!!! Please try again...!!!")


    print()
    print("================================================================")
    ch=input("Enter 1 to select records again or 2  to return back to Main menu: ")
    if ch=='1':
        select_range()





def select_all(): #all function
    print()
    print("\n ~~~SELECT ALL RECORDS~~~ ")
    
    print("=======================================================")
    print("Do you want to select all records from database?")
    print("Press 1 for YES and any key to return back to Main Menu")
    print("=======================================================")
    
    ch=str(input("Enter your choice: "))

    print("=======================================================")
    print()

    if ch=="1":
        connection = mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        cursor = connection.cursor()
        query="select * from alumni"
        cursor.execute(query)
        rs=cursor.fetchall()
        rc=cursor.rowcount
        print("Total Records found :",rc)
        print()
        for r in rs:
            admission_no=  r[0] 
            first_name=    r[1]
            last_name=     r[2]
            dob=           r[3]
            gender=        r[4]                  
            stream=        r[5]
            leaving_year=  r[6]
            profession=    r[7]
            marital_status=r[8]
            home_town=     r[9]
            home_state=    r[10]
            mob_no=        r[11]
            email=         r[12]

            print(" Admission No :    %d" %(admission_no))
            print(" First Name :      %s" %(first_name))
            print(" Last Name :       %s" %(last_name))
            print(" DOB(YYYY-MM-DD) : %s" %(dob))
            print(" Gender(M/F):      %s" %(gender))
            print(" Stream :          %s" %(stream))
            print(" Leaving Year :    %d" %(leaving_year))
            print(" Profession:       %s" %(profession))
            print(" Marital Status :  %s" %(marital_status))
            print(" Home Town :       %s" %(home_town))
            print(" Home State :      %s" %(home_state))
            print(" Mobile No :       %d" %(mob_no))
            print(" E-Mail :          %s" %(email))
            print()
        print("=======================================")
        input("Press Enter to return back to Main Menu: ")
