#module update

import mysql.connector

def update():

    try:
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        mycursor=mycon.cursor()

        print()
        print("~~~Update Menu~~~")
        print("====================================")
        print(" Please enter the following details.")
        print()
        
            
        print("Select the record, that to update.")
        print()
        adm=int(input("Enter Admission Number: "))
        print()
        print("Existing Record:")
        sr="select * from alumni where admission_no='%d' "%(adm)
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
    
        print()
        print("=============================================")
        print()
        ch=input("Enter 1 to continue or 2 to return: ")
        print()
        if ch=='1':
            print("To update, Press following numbers. ")
            print()

            print("1. Update Admission Number")
            print("2. Update First Name")
            print("3. Update Last Name")
            print("4. Update DOB")
            print("5. Update Gender")
            print("6. Update Stream")
            print("7. UpdateLeaving Year")
            print("8. Update Profession")
            print("9. Update Marital Status")
            print("10. Update Home Town")
            print("11. Update Home State")
            print("12. Update Mobile Number")
            print("13. Update E-Mail")
            
            
            

            print()
            choice=input("Select your choice from the above options: ")
            print()

            if choice=='1':
                new=int(input("Enter New Admission Number: "))
                up="update alumni set admission_no={} where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
                
            elif choice=='2':
                new=input("Enter New First Name: ")
                up="update alumni set  first_name='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated!")
            
            elif choice=='3':
                new=input("Enter New Last Name: ")
                up="update alumni set  last_name='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            elif choice=='4':
                new=input("Enter New DOB(dd-mm-yyyy): ")
                up="update alumni set  dob='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
                
            elif choice=='5':
                new=input("Enter New Gender: ")
                up="update alumni set  gender='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
                
            elif choice=='6':
                new=input("Enter New Stream: ")
                up="update alumni set  stream='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
            elif choice=='7':
                new=int(input("Enter New Leaving Year(yyyy): "))
                up="update alumni set  leaving_year={} where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
                
            elif choice=='8':
                new=input("Enter New Profession: ")
                up="update alumni set profession='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")
                
            elif choice=='9':
                new=input("Enter New Marital Status: ")
                up="update alumni set marital_status='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            elif choice=='10':
                new=input("Enter New Home Town: ")
                up="update alumni set  home_town='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            elif choice=='11':
                new=input("Enter New Home State: ")
                up="update alumni set  home_state='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            elif choice=='12':
                new=int(input("Enter New Mobile Number: "))
                up="update alumni set  mob_no={} where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            elif choice=='13':
                new=input("Enter New E-Mail: ")
                up="update alumni set  email='{}' where admission_no ={}".format(new,adm)
                mycursor.execute(up)
                mycon.commit()
                print("Updated")

            else:
                print("Error: Invalid Choice, try again...")
                update()



            
    except:
        print("Something went wrong...!!! Please try again...!!!")



    print("================================================================")
    ch=input("Enter 1 to update another record or 2  to return back to Main menu: ")
    if ch=='1':
        update()
