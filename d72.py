#rename files in folder
import os
files = os.listdir()
i = 1 
for file in files:
    if file.endswith(".txt"):
        os.rename(file,f"file{i}.txt")
        i +=1
print("files renamed")