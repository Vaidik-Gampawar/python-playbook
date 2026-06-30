'''
Ask a number from the user, print the multiplication table upto 10.
'''

i = 1
n = int(input("Enter number: "))

while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1