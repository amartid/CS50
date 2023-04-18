import re

email = input("What's your email? ").strip()#avoid extra spaces

if re.search(r"^[a-zA-Z0-9_ ]+@\w+\.edu$", email): #raw string
    print("Valid")
else:
    print("Invalid")