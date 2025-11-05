#password generator
#Goal:generate random secure password
import random, string
chars = string.ascii_letters + string.digits+string.punctuation
password=''.join(random.choice(chars) 
for _ in range(12))
print("generated password:",password)