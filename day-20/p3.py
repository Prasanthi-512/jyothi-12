#Dict given by the user it must 



n= int(input())
list=[]
for i in range(n):
    user_dict={}
    user_dict['name']=input()
    user_dict['id']=int(input())
    list.append(user_dict)
print(list)
keyword = input()
# l=[]
for j in list:
    if keyword.lower() in j['name'].lower():
        # l.append(i)
        print(j)
    