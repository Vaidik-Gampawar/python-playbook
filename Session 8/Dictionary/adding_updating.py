student = {"name": "vaidik", "age": 22}
print(student)

# Update

student["age"] = 30
print(student)

# Add

student["gender"] = "male"
print(student)

student.update(
    {"city": "pune",
     "state": "maharashtra"
    }
    )
print(student)