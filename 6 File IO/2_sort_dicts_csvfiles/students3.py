students = []
with open("students.csv") as file:
    for line in file:
        name, house= line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house):
    #pass function as argument to another function
    print(f"{student['name']} is in {student['house']}")