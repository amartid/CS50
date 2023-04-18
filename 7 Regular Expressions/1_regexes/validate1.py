email = input("What's your email? ").strip()#avoid extra spaces

if "@"and "." in email :
    print("Valid")
else:
    print("Invalid")
    