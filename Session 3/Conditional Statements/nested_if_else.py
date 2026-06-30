# Age >= 18
# Certificate -> True

age = 23
certificate = False

if age >= 18:
    if certificate == True:
        print("You will be hired")
    else:
        print("Cannot hire, you dont have certificate")
else:
    print("Cannot hire, age is less than 18")