#open a file 
name = input("What's your name? ")

file = open("namesap.txt", "a") # appends to file !!!
file.write(f"{name}\n")
file.close()
