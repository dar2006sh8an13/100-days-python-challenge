#count frequency of elements in a list
number = [10, 20, 4, 45, 99, 10, 20, 4]
freq = {}
for num in number:
   freq[num] = freq.get(num, 0) + 1
print("Frequency of elements in the list:", freq)