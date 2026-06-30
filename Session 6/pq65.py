'''
Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.
'''

def relpace_negative(data):
    result = data
    for i in range(0, len(data)):
        if result[i] < 0:
            result[i] = 0
    return result

numbers = [5, -3, 8, -1, 0, -10, 12]

print(relpace_negative(numbers))
