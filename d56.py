#Password strength checker
import re
password = input("enter password:")
if (len(password)>=8 and re.search(r"[A-z]",password) and re.search(r"[a-z]",password) and re.search(r"[0-1]",password) and re.search(r"[@$₹!%*?&]",password)):
    print("strong password")
else:
    print("weak password")