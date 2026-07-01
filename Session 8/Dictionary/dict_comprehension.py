# squares = {}

# for i in range(1, 6):
#     squares[i] = i * i
# print(squares)

# sqaures = {i : i*i for i in range(1, 6)}
# print(sqaures)


marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

# Keep only subjects where marks > 80
top = {sub: m for sub, m in marks.items() if m > 80}
print(top)

# Transform — double all marks
doubled = {sub: m * 2 for sub, m in marks.items()}
print(doubled)

# Creating a dict from two lists
subjects = ["math", "science", "english"]
scores = [85, 92, 78]

result = {sub: sc for sub, sc in zip(subjects, scores)}
print(result)