
students = [
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]


for student in students:
    print(student["name"]) #print names
    print(student["name"],student["house"]) #print names and houses
    print(student["name"],student["house"],student["patronus"], sep=", ") #print dict with sep


