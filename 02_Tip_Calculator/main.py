print("Welcome to the tip calculator!")
total_bill = int(input ("What was the total bill? $"))
tip_percent = int(input ("How percentage tip would you like to give? 10, 12 or 15? (Please enter only the number without including the percentage sign.) "))
number_of_people = int(input ("How many people to split the bill? "))
tip = round(((total_bill/number_of_people) * (tip_percent/100)), 2)


print(f"Each person should pay ${tip} as a tip")




