#count lines,words&characters in file
with open("notes.txt","r") as file:
    text = file.read()
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
print("lines:",len(lines))
print("words:",len(words))
print("characters:",chars)
    