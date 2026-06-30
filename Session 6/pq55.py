'''
Given a list of numbers, use a loop to calculate and print their average. You can use len() to get the count of elements, but avoid using sum() for the total.
Format the average to two decimal places.
'''

def calculate_avg(lst):
    total = 0
    for i in range(0, len(lst)):
        total = total + lst[i]
    avg = total / len(lst)
    return avg

scores = [85, 90, 78, 92, 88]

ans = calculate_avg(scores)

print(f"Average is {ans:.2f}")