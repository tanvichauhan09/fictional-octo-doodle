#delete module 

import mysql.connector

def delete_record():
    print()
    print("~~~DELETE MENU~~~")
    print("=============================")

    try:
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="Aarsh@23",database="alumni_system")
        mycursor=mycon.cursor()
        adm_no=int(input("Enter the Admission Number: "))
        print()
        print("Existing record:")

        query="select * from alumni where admission_no='%d' " %(adm_no,)
        mycursor.execute(query)
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
        print("Do you want to delete this record")
        ch=int(input("Press 1 for 'YES' or 2 for 'NO' : "))
        print()
        if ch==1:

            sd="delete from alumni where admission_no='%d' " %(adm_no,)
            mycursor.execute(sd)
            mycon.commit()

            print("Record is deleted")
            
        elif ch==2:
            print("Record is safe")
            
        else:
            print("Invalid Input")


    except:
        print("Database not exist.")
        
    print()
    print("================================================================")
    ch=input("Enter 1 to delete another record or 2  to return back to Main menu: ")
    if ch=='1':
        delete_record()
