
#this is an tip calculator program
print("Welcome to the tip calculator")
bill = float(input("What is the total bill amount? \n"))
member = float(input("How many members dined? \n"))
tips = float(input("What percentage tip do you like to give? 10, 12 or 15?\n"))
tip_as_percent = tips / 100
total_tip = bill * tip_as_percent
print(f"Your Total tip is \n {total_tip}")
total_bill = total_tip + bill
print(f"Your Toatl bill is \n{total_bill}")
member_tips = total_bill / member
member_bill= round(member_tips, 2)
member_bill = "{:.2f}".format(member_bill)
print(f"Each person should pay {member_bill}")