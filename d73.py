#copy file content to another file
with open("input.txt")as file1,open("output.txt","w") as file2:
    file2.write(file1.read())
print("copied successfully")
    