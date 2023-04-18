email = input("What's your email? ").strip()#avoid extra spaces

username,domain = email.split("@")
#returns user and domain! 
if username: #if has characters
    print("Valid")
else:
    print("Invalid")