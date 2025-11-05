with open("sample.txt")as f:
    lines = f.readlines()
with open("clean.txt","w")as f:
    for line in lines:
        if line.strip():
            f.write(line)
