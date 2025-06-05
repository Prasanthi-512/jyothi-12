def add_student(gradebook):
    name=input("Enter name: ")
    mark_list = list(map(int,input("Enter marks: ").split()))
    gradebook[name]=mark_list
    print(gradebook)


def view_student(gradebook):
    # for i in gradebook:
    #     print(f"{i}: {gradebook[i]}")
    for name, marks in gradebook.items():
        avg = sum(marks) / len(marks)
        print(f"{name} - Marks: {marks} - Avg: {avg:.2f}")



def search_student(gradebook):
    name_to_search=input("Enter name to search: ")
    for name, marks in gradebook.items():
        if name_to_search in name:
            avg = sum(marks) / len(marks)
            print(f"{name} - Marks: {marks} - Avg: {avg:.2f}")
            break
        else:
            print("Not found")


def update_student(gradebook):
    name_to_update=input("Enter name: ")
    if name_to_update in gradebook:
        mark_list = list(map(int,input("Enter marks: ").split(" ")))
        gradebook[name_to_update]=mark_list
        print(f"{name_to_update} marks updated")
    else:
        print("Not found")


def remove_student(gradebook):
    name_to_remove=input("Enter name to remove: ")
    if name_to_remove in gradebook:
        del gradebook[name_to_remove]
        print(f"{name_to_remove}  remove")
    else:
        print("Not found")