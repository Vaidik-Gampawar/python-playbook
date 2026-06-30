# 1 to 10, but only even numbers

# new_list = [i for i in range(1, 10) if i%2 == 0]
# print(new_list)


# From 1 to 100, make list of all prime numbers

def is_prime(num):
    factor = 0
    for i in range(1, num+1):
        if num%i == 0:
            factor = factor + 1
    if factor == 2:
        return True
    return False        

new_list = [i for i in range(1, 101) if is_prime(i) == True]
print(new_list)