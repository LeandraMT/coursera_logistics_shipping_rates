# Shipping Cost Calculator

weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate the shipping cost
shipping_cost = weight * rate

print(f"shipping Cost {shipping_cost} USD")
