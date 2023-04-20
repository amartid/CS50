# 
#
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

#dictionaries are mutable  !
    
def get_student(): #dict
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house":house}


    
if __name__== "__main__":
    main()