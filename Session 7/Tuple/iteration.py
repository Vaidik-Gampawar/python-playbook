my_tuple = (1, 2, 3, "Vaidik")

for i in range(0, len(my_tuple)):
    print(my_tuple[i])

for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")

for i in my_tuple:
    print(i)