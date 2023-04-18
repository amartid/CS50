#open a file 
name = input("What's your name? ")

with open("namesap.txt", "a") as file: #closes the file
    file.write(f"{name}\n")
