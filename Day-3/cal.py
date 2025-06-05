import ope
n1=int(input())
while True:
    op=input()
    if op=="=":
        #print(n1)
        break
    n2=int(input())
    if op == "+":
        n1=ope.add(n1,n2)
    elif op == "-":
        n1=ope.sub(n1,n2 )
    elif op == "*":
        n1=ope.mul(n1,n2)
    elif op == "/":
        n1=ope.div(n1,n2)
    elif op == "**":
        n1=ope.exp(n1,n2)
    elif op == "%":
        n1=ope.mod(n1,n2) 
    #print(n1)
print("End of the result: ",n1)