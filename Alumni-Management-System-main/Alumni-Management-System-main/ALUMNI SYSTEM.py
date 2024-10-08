#Main Program

import main_menu
import registration
import update
import selection
import delete

print("=========================================================================================================")
print("\n\t\t\t\t Welcome To The School Alumni System ")
print("=========================================================================================================")

print("\n\t\t\t\t Designed & Devloped by: Aarsh Saxena & Salman Khan ")
print("\t\t\t\t 12th Science-A, DPS Bareilly ")


while True:
    main_menu.main_menu()
    op=str(input("Enter your chosen category: "))

    if op=='1':
        registration.register()
        
    elif op=='2':
        update.update()
        
    elif op=='3':
        selection.select_record()

    elif op=='4':
        selection.select_range()
        
    elif op=='5':
        selection.select_all()
        
    elif op=='6':
        delete.delete_record()
    elif op=='7':
        break
    else:
        print()
        print("***Invalid. Please try again...***")

print()
print("\n\t\t\t\t Designed & Devloped by: Aarsh Saxena & Salman Khan ")
print("\t\t\t\t 12th Science-A, DPS Bareilly ")
end=input("Press Enter Again, to Exit")
