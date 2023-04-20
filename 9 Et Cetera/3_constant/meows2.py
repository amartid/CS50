class Cat:
    MEOWS = 3
    
    def meows(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()

cat.meows()