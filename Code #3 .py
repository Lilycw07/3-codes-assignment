
# Get user input
destination = input("Where are you traveling to? ")
distance = float(input("Enter the distance to your destination in miles: "))
speed = float(input("Enter your average speed in miles per hour: "))

# Arithmetic calculation
time = distance / speed  # time = distance ÷ speed

# Output the result
print("\nYour trip to", destination, "will take about", round(time, 2), "hours.")

