'''
Write a function fizzbuzz(n) that takes a single number and prints "Fizz" if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible by both, otherwise print the number itself.
'''

def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        if n % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")

fizzbuzz(5)