# Make a function which return min and max of a list

def min_max(lst):
    mini = min(lst)
    maxi = max(lst)

    return mini, maxi

ans1, ans2 = min_max([34, 34, 56, 64, 3, 53, 55])
print(ans1, ans2)
