print("Welcome to the Tip Calculator!")

total_bill = float(input("What whas the total bill? $"))
tip_percent = int(input("How much tip would you like to give? \'Common Tips: 10, 12, 15\'\n"))
people_to_split = int(input("How many people to split the bill? "))

your_share = (total_bill / people_to_split) * (1 + (tip_percent / 100))

print(f"Each person should pay: ${'{0:.2f}'.format(your_share)}")
