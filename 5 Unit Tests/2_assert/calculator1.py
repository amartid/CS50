from calculator import square

def main():
    test_square()

def test_square():
    # what kind of tests can i do?
    assert square(2) ==4
    assert square(3) ==9


if __name__== "__main__":
    main()
# we get assertionError !