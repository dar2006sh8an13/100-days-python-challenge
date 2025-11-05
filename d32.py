#recursive factorial function
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
num = int(input("enter a number: "))
print("factorial(recursive):",factorial_recursive(num))