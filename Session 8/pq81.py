'''
Construct a dictionary containing four product names and their
prices. Prompt the user to enter a product name. Use the in
keyword to check if it exists; if so, display its price. Otherwise,
inform the user "Product not found."
'''

product = {
    "Macbook": 80000,
    "Watch": 40000,
    "Ipod": 35000,
    "Ipad": 56000
}

n = input("Enter product name: ")

if n in product.keys():
    print(f"{n}: {product[n]}")
else:
    print("Product not found.")