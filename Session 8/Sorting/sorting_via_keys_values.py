marks = {
    "science": 76,
    "maths": 80,
    "english": 56,
    "sst": 90
}

ans = dict(sorted(marks.items(), key = lambda x:x[1]))
print(ans)
