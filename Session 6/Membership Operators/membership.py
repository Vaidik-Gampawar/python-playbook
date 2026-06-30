lst = [12, 23, 54, 32, 42, 67, 21, 86, 76, 45, 77]

target = int(input("Enter targer: "))

if target in lst:
    lst.remove(target)
else:
    print("Target does not exists")

print(lst)