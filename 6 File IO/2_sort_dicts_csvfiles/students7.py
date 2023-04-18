import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    # returns dictionaries one at a time
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    #pass function as argument to another function
    print(f"{student['name']} is from {student['home']}")