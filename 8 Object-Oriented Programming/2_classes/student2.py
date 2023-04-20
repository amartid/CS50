# class

class Student:
    #classe - methods . An object is an instance of a class !
    def __init__(self, name, house):#customise class objects
        #self gives you access to the current object that you created
        self.name = name
        self.house = house
        
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

#dictionaries are mutable  !
    
def get_student(): #dict
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

    
if __name__== "__main__":
    main()

    