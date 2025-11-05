#Word frequency Counter
from collections import counter
with open("sample.txt","r") as file:
    words = file.read().lower().split()
count = counter (words())
print(count)