'''
Given a dictionary of marks for different subjects, loop over its values()
to calculate and print the total marks and the average mark obtained.
'''

marks = {
    "science": 89,
    "maths": 65,
    "english": 78,
    "sst": 92,
    "comp": 34
}

total = 0
subjects = 0
for marks in marks.values():
    total = total + marks
    subjects += 1

avg_marks = total / subjects

print(f"Total Marks: {total}\nAverage Marks: {avg_marks}")