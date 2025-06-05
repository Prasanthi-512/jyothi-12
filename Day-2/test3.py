n1=int(input())
#op=input()
#n2=int(input())
while True:
    op=input()
    if op=="=":
        print(n1)
        break
    n2=int(input())
    if op=="+": #or op=="-" or op=="*" or op=="/":
        n1=n1+n2
    elif op=="-":
        n1=n1-n2
    elif op=="*":
        n1=n1*n2
    elif op=="/":
        n1=n1/n2
    else:
        n1="Invalid operator"