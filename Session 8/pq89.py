'''
Given a dictionary of subjects and their marks, sort it by marks in descending
order. Then, print only the top 3 subjects with the highest marks.
'''

subjects = {
    "science": 76,
    "maths": 80,
    "english": 56,
    "sst": 90,
    "comp": 89,
    "sports": 100
}

ans = sorted(subjects.items(), key= lambda x: x[1], reverse=True)
result = ans[0:3]

for sub, mark in result:
    print(f"sub = {sub}, marks = {mark}")