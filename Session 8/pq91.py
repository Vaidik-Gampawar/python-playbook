'''
Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that includes
only the subjects where the student scored 40 or more (i.e., passed).
'''

subjects = {
    "science": 76,
    "maths": 32,
    "english": 56,
    "sst": 24,
    "comp": 12,
    "sports": 100
}

new_dict = {sub: sc for sub, sc in subjects.items() if sc > 40}
print(new_dict)