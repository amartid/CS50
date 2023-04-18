import re

email = input("What's your email? ").strip()#avoid extra spaces

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): #raw string
    print("Valid")
else:
    print("Invalid")