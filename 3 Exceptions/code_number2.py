# Try exceptional cases

try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")