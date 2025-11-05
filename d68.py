#Search in file system
#goal:search a word inside a file
word = input("enter word to search:")
with open ("sample.txt","r") as file:
    text = file.read()
if word in text:
    print("word found")
else:
    print("not found")