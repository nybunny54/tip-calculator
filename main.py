

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ " )) 
tip = int(input("What persentage tip would you like to give 10,12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill +total_tip_amount

bill_per_person = total_bill/people

total_round = round(bill_per_person,2)
total_round = "{:.2f}".format(bill_per_person)

print(f"Each person should pay : ${total_round}")