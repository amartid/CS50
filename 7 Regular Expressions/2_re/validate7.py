import re

email = input("What's your email? ").strip()#avoid extra spaces

if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")