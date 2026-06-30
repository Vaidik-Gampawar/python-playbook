lst = [12, 23, 54, 32, 42, 67, 21, 86, 76, 45, 77]

# Sort vs Sorted

new_list = sorted(lst)
print(f"new_list = {new_list}, id = {id(new_list)}")

print(lst)

lst.sort()

print(lst)