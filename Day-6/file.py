# file=open("./data1.txt","w")
# file.writelines(['prasanthi take 45 days trainng \n'
# 'enjoying the class \n'
# 'Thank you'])
# print(file.writelines)



file=open("./data1.txt","r")
n=file.readlines()
file.close()
print(n)

list_data=n.split("\n")
age_dict={}
for item in list_data:
    splitted_item = item.split(" ")
    age_dict[splitted_item[0]]=int(splitted_item(1))
    print(age_dict)




