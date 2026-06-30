'''
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
'''

def min_max(x, y, z):
    if x > y and x > z:
        print(f"{x} is largest")
    elif y > x and y > z:
        print(f"{y} is largest")
    elif z > x and z > y:
        print(f"{z} is largest")
    else:
        print("All three are equal")

min_max(2, 5, 2)