import re

email = input("What's your email? ").strip()#avoid extra spaces

if re.search(r"^[^@]+@[^@]+\.edu$", email): #raw string
    print("Valid")
else:
    print("Invalid")