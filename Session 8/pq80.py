'''
Define a dictionary with five subjects and their respective marks.
Utilize the get() method to try accessing a subject that is not in the
dictionary, ensuring it prints "Not Available" as a default.
'''

marks = {
    "science": 76,
    "maths": 80,
    "english": 56,
    "sst": 90
}

sub = input("Enter subject: ")

if marks.get(sub) not in marks.values():
    print("Not Available")
else:
    print("Available")