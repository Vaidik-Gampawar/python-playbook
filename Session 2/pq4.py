'''
A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string
'''

math = int(input("Enter math's marks: "))
science = int(input("Enter science marks: "))
sst = int(input("Enter sst marks: "))

total_marks = math + science + sst
average = total_marks / 3

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average}")