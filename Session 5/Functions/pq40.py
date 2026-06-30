'''
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
'''

def discount(orginal_price, discount_percent):
    discount_price = discount_percent/100 * orginal_price
    final_amount = orginal_price - discount_price
    
    print(f"Orginal Price:{orginal_price}\nDiscount Percent:{discount_percent}\nDiscount Price:{final_amount}")

discount(100, 20)