# Prints a word in uppercase

def main():
    yell("This","is","CS50", "yo")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()