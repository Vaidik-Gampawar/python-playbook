'''
Create a dictionary of 6 subjects and their respective marks. Print the subject
with the highest marks and the one with the lowest, using max() and min()
functions alongside a lambda expression.
'''

subjects = {
    "science": 76,
    "maths": 80,
    "english": 56,
    "sst": 90,
    "comp": 89,
    "sports": 100
}

highest = max(subjects.items(), key= lambda x: x[1])
lowest = min(subjects.items(), key= lambda x: x[1])
print(highest)
print(lowest)

