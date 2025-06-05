n1=float(input("Enter first number: "))
operator=input("Enter operator: ")
n2=float(input("enter second number: "))
#if operator!="=":
if operator=="+":
    result=n1+n2
elif operator=="-":
    result=n1-n2
elif operator=="*":
    result=n1*n2
elif operator=="/":
    result=n1/n2
else:
    result="invaild operator"
print(f"{n1}+{n2}= ",result)