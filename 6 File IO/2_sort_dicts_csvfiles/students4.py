students = []
with open("students.csv") as file:
    for line in file:
        name, house= line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
#lambda

for student in sorted(students, key=lambda student: student["name"]):
    #pass function as argument to another function
    print(f"{student['name']} is in {student['house']}")