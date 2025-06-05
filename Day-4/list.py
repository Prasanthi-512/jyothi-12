#a="apple"
#a_list=list(a)
#print(a_list)


my_list1=["suguna","prasanthi","baby"]
my_list2=[10,20,30]
my_list1.append("sailu")
print("After append: ",my_list1)
my_list1.remove("baby")
print("After remove: ",my_list1)
my_list1.insert(0,"malli")
print("After insert: ",my_list1)
my_list1.pop(1)
print("After pop: ",my_list1)
my_list2.extend(my_list1)
print(my_list1)
my_list1.clear()
print(my_list1)