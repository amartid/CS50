import csv

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        #returns lists one at a time
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    #pass function as argument to another function
    print(f"{student['name']} is from {student['home']}")