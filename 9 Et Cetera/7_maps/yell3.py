# Prints a word in uppercase

def main():
    yell("This","is","CS50", "yo")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()