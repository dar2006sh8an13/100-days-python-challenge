#email sender 
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("youremail@gmail.com", "your_app_password")

server.sendmail("youremail@gmail.com", "receiver@gmail.com", "Hello from Python!")
print("Email Sent ✅")
