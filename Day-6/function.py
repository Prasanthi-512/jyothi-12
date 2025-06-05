
# data=open("./mydata","a")
# print(data)
def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    with open("mydata.txt", "a") as file:
        file.write(f"name: {name} ,mobile: {mobile}\n")
    # print("Contact added successfully!")


def view_contacts(contacts):
    print("\n")
    for i in contacts:
        #print(f"{i} : {contacts[i]}")
        with open("mydata.txt", "r") as file:
            file.readlines("Contact viewed")
    
def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)
    with open("mydata.txt", "a") as file:
        file.write()
    # print("Contact deleted successfully!")



def find_contact(contacts):
    name_to_find = input("Enter name to Find :")
    found=False
    for i in contacts:
        if name_to_find in i:
            print(f"found contact is :{name_to_find} : {contacts[name_to_find]}")
            found=True
        if not found:
            print("Contact not found")
    with open("mydata.txt", "a") as file:
        file.write(f"{name_to_find}\n")



def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " ,  name_to_edit)
    with open("mydata.txt","a") as file:
        file.write(f"{name_to_edit}\n")
   