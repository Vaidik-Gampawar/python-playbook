'''
Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
'''

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

if num1 > num2:
    print("num1 is greater than num2")
elif num2 > num1:
    print("num2 is greater than num1")
else:
    print("Both are equal")