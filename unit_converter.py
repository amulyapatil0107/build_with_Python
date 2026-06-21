# Simple Unit Converter

print("UNIT CONVERTER")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print("Miles:", round(miles, 2))

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", round(fahrenheit, 2))

elif choice == 3:
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print("Pounds:", round(pounds, 2))
