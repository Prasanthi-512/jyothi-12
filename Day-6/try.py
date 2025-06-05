try:
    a=int(input())
    b=int(input())
    result=a/b
    print(result)
except Exception as e:
    print(f"{e} is a error")
# except ZeroDivisionError:
#     print("It is not divisible by zero")
# except ValueError:
#     print("value error")
else:
    print("The code is executed successfully")
finally:
    print("Thank you")