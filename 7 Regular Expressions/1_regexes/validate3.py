email = input("What's your email? ").strip()#avoid extra spaces

username,domain = email.split("@")
#returns user and domain! 
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")