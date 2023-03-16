#round final answer to 2 decimal places
print("Welcome to the tip calculator")
total_bill = input("What is your total bill: ")
total_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
a = (float(total_tip)/ 100)+ 1
b = float(total_bill) * a
total_people = input("How many people to split the bill with: ") 
c = round((b/ int(total_people)),2)
bill = print(f"Each person should pay:{c}")