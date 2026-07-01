'''
You have two separate lists: one containing subject names and another containing corresponding marks. Create a dictionary from these two
lists using dictionary comprehension, mapping each subject to its mark
'''

subjects = ["science", "maths", "comp"]
score = [78, 99, 67]

new_dict = {sub: sc for sub, sc in zip(subjects, score)}
print(new_dict)