#open a file 
name = input("What's your name? ")

file = open("namesa.txt", "a") # appends to file !!!
file.write(name)
file.close()
