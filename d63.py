#json file read
#Goal:read json student data
import json
with open("data.json","r")as file:
    data = json.load(file)
    print(data)