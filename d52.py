#file word counter
with open("sample.txt","r") as file:
    text = file.read()
words = text.split()
print(f"total words:{len (words)}")