print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = (int(input("What percentage tip would you like to give? 10 12 15 ")))
people = int(input("How many people to split the bill? "))

tip_percentage = (tip /100)
total_Bill=(((bill*tip_percentage)+bill)/people)
total_bill = round(total_Bill, 2)
print(f"Your total bill is = {total_bill}")




