student = {
    "name": "vaidik", 
    "age": 22,
    "city": "pune",
    "state": "maharashtra" 
}
print(student, id(student))

# student.pop("name")
# student.clear()

# del student

del student["age"]

print(student, id(student))