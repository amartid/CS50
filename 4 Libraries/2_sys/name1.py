import sys
# if i dont type an argument then i have error

# IndexError: list index out of range
try:
    print("hellp, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
