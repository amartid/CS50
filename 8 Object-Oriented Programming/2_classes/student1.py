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
    student = Student(name, house) #passing arguments/values to the function
    #uses Student class as a template !
    #object exist on memory
    return student

    
if __name__== "__main__":
    main()

    