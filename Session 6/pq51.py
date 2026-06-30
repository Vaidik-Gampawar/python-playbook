'''
Create a list of 6 hypothetical student marks (e.g., [75, 88, 62, 91, 70, 83]). Using built-in functions, print the highest mark, lowest mark, total sum of marks, and the average mark.
Format the average to two decimal places.
'''

marks = [75, 88, 62, 91, 70, 83]

def min_max_sum(data):
    mini = min(marks)
    maxi = max(marks)
    total = sum(marks)

    return mini, maxi, total

mini, maxi, total = min_max_sum(marks)
print(f"Highest Mark: {maxi}\nLowest Mark: {mini}\nTotal Marks: {total}\nAverage Marks: {total/len(marks):.2f}")