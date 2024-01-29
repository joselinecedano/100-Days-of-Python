#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


#Input Requests and Message
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
guests = int(input("How many people to split the bill?\n"))

#Calculations
tip_to_percent = tip / 100
total_tip = bill * tip_to_percent
total_bill = bill + total_tip
bill_per_guest = total_bill / guests

#Rounding
total = round(bill_per_guest, 2)
#2 because we want to round to 2 decimal places

#Final Message 
print(f"Each person should pay: ${total:.2f}")
#The :.2f is to round to 2 decimal places since we were getting a formatting error before (33.6 instead of 33.60))