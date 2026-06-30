'''
A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
'''

amount = eval(input("Enter amount: "))

if amount >= 5000:
    print(f"{(20 / 100) * amount} saved")
elif amount >= 2000:
    print(f"{(10 / 100) * amount} saved")
elif amount >= 1000:
    print(f"{(5 / 100) * amount} saved")
else:
    print("Discount not applied")

