item = input("What do you want to save for? ")
price = float(input("How much does it cost? $"))
savings_per_week = float(input("How much money will you save each week? $"))


weeks_needed = price / savings_per_week


print("To buy your", item, "you'll need about", round(weeks_needed, 1), "weeks of saving.")

