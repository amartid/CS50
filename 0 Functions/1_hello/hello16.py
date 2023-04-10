#STR
#docs.python.org/3/library/stdtypes.html#string-methods

# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last
first, last= name.split(" ")

# Say hello to user
print(f"hello, name,{name}")
#special string with f in front !