# Logical operators are used to combine multiple conditions together.
'''
Operator     Meaning               Returns True when
and          Both conditions       Both are True
or           Either condition      At least one is True
not          Opposite              Original is False
'''

chemistry = 11
physics = 31

print(chemistry > 33 and physics > 33)
print(chemistry > 33 or physics > 33)
print(not chemistry > 33 and not physics > 33)
print(not (chemistry > 33 and physics > 33))