# class

class Student:
    ...# invent a new datatype ! 

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

#dictionaries are mutable  !
    
def get_student(): #dict
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

    
if __name__== "__main__":
    main()

    