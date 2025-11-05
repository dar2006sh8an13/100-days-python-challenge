#handle divide by zero exception
try:
    a = int(input("enter numerator: "))
    b = int(input("enter denomitor: "))
    print("result:",a/b)
except ZeroDivisionError:
    print("error: cannot divide by zero!")
