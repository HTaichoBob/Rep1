def calculate_price(original_price, discount_rate=0.10):
    discount_amount = original_price * discount_rate
    final_price = original_price - discount_amount
    return final_price


original_price = float(input("Enter the original price: $"))
print("The discount rate is 10%")
final_price = calculate_price(original_price,0.1)

print(f"Final price is $", final_price)