email = input("What's your email? ").strip()#avoid extra spaces

if "@" in email:
    print("Valid")
else:
    print("Invalid")
    