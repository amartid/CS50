#open a file 

with open("namesap.txt", "r") as file: #reads
    lines = file.readlines() #returns as list

for line in lines:
    print("hello,", line)

    #line.rstrip())
    #line, end="")