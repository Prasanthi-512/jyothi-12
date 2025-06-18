def name(email):
    if email in '@' and email in '.':
        return True
    else:
        return False

email= input()
n=email[1:len(email)-1]
print(n)
# if "@" and "." in n:
#     print("valid")
# else:
#     print("not vaild")

