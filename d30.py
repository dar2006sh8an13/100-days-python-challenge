#writing to a file 
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
with open("example.txt", "a") as file:
    print(file.read())