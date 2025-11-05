#Find the Largest Element in a List
number = [12, 45, 23, 67, 34, 89, 22]
largest = number[0]
for num in number:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)