#count characters,words& lines in file
with open("sample.txt")as file:
    text = file.read()
print("characters:",len(text))
print("words:",len(text.split()))
print("lines",len(text.splitlines()))
