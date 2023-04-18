#open a file 

with open("namesap.txt", "r") as file: #reads
    for line in file:
        print("hello,", line.rstrip())
        