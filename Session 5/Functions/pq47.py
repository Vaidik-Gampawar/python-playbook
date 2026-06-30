'''
Write a function power(base, exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
'''

def power(base, exp):
    total = 1
    for i in range(exp):
        total *= base
    return total

print(power(2, 3))