with open("notes.txt","a") as file:
    text = input ("enter text to append:")
    file.write(text+"\n")
    print("data appended successsfully!")

with open("notes.txt","r") as file:
    print(file.read())
