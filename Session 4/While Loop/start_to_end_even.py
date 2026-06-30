# Start to End Print Even Numbers

start = int(input("Enter starting number: "))
end = int(input("Enter end number: "))

i = start

while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1
