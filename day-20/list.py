# list=input().split()
# print(list)


n= int(input())
name_list=[]

for i in range(n):
    name= input()
    name_list.append(name)
    print(name_list)

keyword = input()
l=[]
for i in list:
    if keyword.lower() in  i.lower():# filtering case insenstively
        l.append(i)
        print(i)
# print(l)