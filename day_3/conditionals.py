
#that is a python condional
#you can do conditionals inside condionals
#condition to ride a rollercoaster
print("welcome to the rollercoaster")
bill=0
height=int(input("What is your height in cm? "))
if height >=120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill=5
        print("Please pay $5.")
    elif age <= 18:
        bill=7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is gonna be ok.Have a free ride on us!")
    else:
        bill=12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo =="Y":
        bill +=3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


# ficar ligado ao usar os sinais logicos maior ou menor, sempre tentar colar entre os valores
# logical operators or, and, not