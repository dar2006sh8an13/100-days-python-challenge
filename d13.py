#Palindrome Number
num = str(input("Enter a number: "))
rev = str(num)[::-1]
if str(num)==rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")