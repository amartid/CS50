students = []
with open("students1.csv") as file:
    for line in file:
        name, home= line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)
#lambda

for student in sorted(students, key=lambda student: student["name"]):
    #pass function as argument to another function
    print(f"{student['name']} is from {student['home']}")