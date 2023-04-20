# Prints a word in uppercase

def main():
    yell(["This","is","CS50", "yo"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()