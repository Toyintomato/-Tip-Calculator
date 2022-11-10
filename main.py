print("Welcome to Tip Calculatorrrrr!!!!!!!!\n")
total_bill = float(input("What was the total bill?\n"))
per_tip = float(input("What percentage tip would you like to give 10, 12 or 15?\n"))
split_btw = int(input("How many people to split the bill?\n"))
per_tip_calc = per_tip / 100 * total_bill + total_bill
each_payment = round((per_tip_calc / split_btw), 2)
print(f"Each person should pay N{each_payment}  ")