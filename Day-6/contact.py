import function as cf
contacts = {}
data=contacts
# data=open("./mydata.txt","r")
# n=data.readlines()
# data.close()
# print(n)


print("\tContacts App")

while True:
    try:
        print("\n\nChoices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            cf.add_contact(contacts)
        elif choice == 2:
            cf.view_contacts(contacts)
            with open("mydata.txt", "r") as file:
                x=file.read()
                print(x)

        elif choice == 3:
            cf.delete_contact(contacts)
        elif choice == 4:
            cf.find_contact(contacts)
        elif choice == 5:
            cf.edit_contact(contacts)
        else:
            print("Ok bye thank you!!!")
            break 
    except:
        print("Error occured")
    finally:
        print(".....Contact App......")