'''
Create a dictionary mapping five countries to their capital cities. Iterate
through this dictionary using the items() method and print each pair in
the format: Country → Capital.
'''

countries = {
    "India": "New Delhi",
    "South Africa": "Seoul",
    "England": "London",
    "Japan": "Tokyo",
    "Cananda": "Ottawa"
}

for key, values in countries.items():
    print(f"{key} -> {values}")