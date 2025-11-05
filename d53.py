#email slicer
email = input("enter your email:")
username,domain = email.split("@")
print(f"username:{username}\ndomain:{domain}")