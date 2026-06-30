'''
Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
'''

def find_min(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < y:
        return z

ans = find_min(2, 5, 6)
print(ans)
