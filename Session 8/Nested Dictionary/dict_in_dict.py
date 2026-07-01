students = {
 "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
 "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
 "103": {"name": "Karan", "age": 22, "city": "Pune"}
}


# How to access
# print(students["103"])
# print(students["103"]["age"])
# print(students["103"]["details"]["phone"])

total = 0
for roll, details in students.items():
    print(f"{roll} -> {details["name"]} -> {details["age"]}")
    total = total + details["age"]

print(total)