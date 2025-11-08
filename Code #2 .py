item = input("What do you want to save for? ")
price = float(input("How much does it cost? $"))
savings_per_week = float(input("How much money will you save each week? $"))

# Arithmetic operation
weeks_needed = price / savings_per_week

# Display the result
print("To buy your", item, "you'll need about", round(weeks_needed, 1), "weeks of saving.")
