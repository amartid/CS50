
# Define the main
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

# Define a function to calculate the square of a number
def square(n):
    return n+n

# This is the standard Python idiom to check if the current file is being run as the main program.
# If so, it calls the main() function, but if it's being imported as a module, main() won't be executed.
if __name__== "__main__":
    main()
