#Sum of Natural Numbers
n = int(input("enter a number:    "))
total= 0
for i in range(1,n+1):
    total += i
print("The sum of first", n, "natural numbers is:", total)