import gradefun as gf
gradebook={}
while True:
    print("1.Add student: ")
    print("2.View student: ")
    print("3.Search student: ")
    print("4.Update student: ")
    print("5.Remove student: ")
    print("6.Exit")

    choose=int(input(" \n \nChoose any one : "))
    if choose == 1:
        gf.add_student(gradebook)
    elif choose == 2:
        gf.view_student(gradebook)
    elif choose == 3:
        gf.search_student(gradebook)
    elif choose == 4:
        gf.update_student(gradebook)
    elif choose == 5:
        gf.remove_student(gradebook)
    else:
        print("Thank you")
        break 