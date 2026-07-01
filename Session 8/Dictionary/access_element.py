marks = {
    "science": 98,
    "maths": 54,
    "comp": 56,
    55: 100,
    101: "Vaidik",
    "abc": [1, 2, 3, 4]
}

# print(marks[55])
# print(marks["abc"])

# print(marks.get("science", 0))

subject = "history"

ans = marks.get(subject)
if ans is None:
    print("Subject Not Found")
else:
    print(f"Marks Scored: {ans}")