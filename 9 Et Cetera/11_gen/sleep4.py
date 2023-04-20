# Adds main


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        yield "🐑" *i
        # generate a piece of data at a time !


if __name__ == "__main__":
    main()