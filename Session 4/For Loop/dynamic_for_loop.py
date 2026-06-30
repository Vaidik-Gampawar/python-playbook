# Dynamic for loop

start = int(input("Enter starting number: "))
end = int(input("Enter end number: "))

if start < end:
    for i in range(start, end+1):
        print(i, end=" ")
elif start > end:
    for i in range(start, end-1, -1):
        print(i, end=" ")