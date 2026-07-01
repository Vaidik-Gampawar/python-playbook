'''
Write a Python function named merge_dicts(d1, d2) that accepts two
dictionaries (d1 and d2) as arguments and returns a new dictionary
formed by merging them using the update() method. Ensure d1 remains
unchanged.
'''

def merge_dicts(d1, d2):
    new_dict = {}
    for key, value in d1.items():
        new_dict.update({key: value})
    for key, value in d2.items():
        new_dict.update({key: value})
    return new_dict

d1 = {
    "name": "vaidik",
    "age": 21
}

d2 = {
    "city": "pune",
    "gender": "male"
}

print(merge_dicts(d1, d2))
