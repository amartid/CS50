import re

email = input("What's your email? ").strip()#avoid extra spaces

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #raw string
    print("Valid")
else:
    print("Invalid")