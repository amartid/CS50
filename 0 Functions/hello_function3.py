# calling parammetre to
# give default value to a a parammetre

hello()
name = input("What's your name? ")
# passing as input the name
hello(name)


def hello(to="world"):
    print("hello",to)

# ERROR 
# function must exists by the time i am using it