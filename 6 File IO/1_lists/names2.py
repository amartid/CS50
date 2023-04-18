#open a file 
name = input("What's your name? ")

file = open("names.txt", "w") # recreates the file !!!
file.write(name)
file.close()
