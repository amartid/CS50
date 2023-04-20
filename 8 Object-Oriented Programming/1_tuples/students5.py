#tuple !
# tuple is immutable cant change values !
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
        #returns error tuple cant change the value of tupple!
    print(f"{student[0]} from {student[1]}")

    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #changed to list
    #mutability ! !!
    
if __name__== "__main__":
    main()