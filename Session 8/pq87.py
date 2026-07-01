'''
Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print the full
details of each student in a clear, readable format.
'''

students = {
    101: {"name" : "vaidik", "age": 21, "city": "pune"},
    102: {"name" : "lobhas", "age": 23, "city": "delhi"},
    103: {"name" : "sumit", "age": 22, "city": "cpur"},
    104: {"name" : "faiz", "age": 21, "city": "bpq"},
}

for key, values in students.items():
    print(f"Roll No: {key} -> {values["name"]} -> {values["age"]} -> {values["city"]}")