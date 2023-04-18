#open a file 
names = []
with open("namesap.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())