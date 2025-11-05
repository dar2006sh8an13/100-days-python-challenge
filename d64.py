#json file write
#goal:store student info in json
import json
student = {"name":"darshan","usn":"1sv24ai010","branch":"AIML"}
with open("data.json","w")as file:
    json.dump(student,file,indent=4)
print("json saved!")