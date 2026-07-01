student = {
    "name": "vaidik", 
    "age": 22,
    "city": "pune",
    "state": "maharashtra" 
}

# print("age" in student)
# print(35 in student)

k = input("Enter key: ")

if k in student:
    print(student[k])
else:
    print("Key does not exists")