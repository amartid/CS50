# calling parammetre to
# give default value to a a parammetre
def hello(to="world"):
    print("hello",to)

hello()
name = input("What's your name? ")
# passing as input the name
hello(name)
