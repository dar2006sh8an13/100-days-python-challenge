#simple interest calculator
p = float(input("enter principal:"))
r = float(input("enter rate of interest:"))
t = float(input("enter time (in years):"))
si = (p*r*t)/100
print(f"simple interest:{si}")