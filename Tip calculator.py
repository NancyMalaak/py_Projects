print("Welcome to the tip calculator.")
bill = float (input ("What was the total bill?$"))
tip = int ( input( " What percentage tip would you like to give ? 10 , 12, or 15?"))
percentage= tip/100
people= int(input("How many people to slipt the bill?"))
total_bill= bill* percentage
total_bill_with_tip= bill+ total_bill
bill_per_person= total_bill_with_tip/ people
final_amount= round(bill_per_person, 2)
print(f"Each person should pay : ${final_amount}")