print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? "))
tip=int(input("What porcentage tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people to split the bill? "))
tip=tip/100 + 1
bill_per_person=round((bill* tip)/people,2)
print(f"Each person should pay: ${bill_per_person}")
