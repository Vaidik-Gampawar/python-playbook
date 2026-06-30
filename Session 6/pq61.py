'''
Given a list, remove all duplicate elements while
preserving the original order of the unique items.
'''

data = [10, 20, 30, 20, 10, 40, 50, 40]
# Expected output: [10, 20, 30, 40, 50]

def remove_duplicates(data):
    result = []
    for i in data:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicates(data))
        