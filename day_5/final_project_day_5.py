print("Welcome to the password Generator")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
size_letters = int(input("How many letters would you like in your password? "))
size_symbols = int(input("How many symbols would you like? "))
size_numbers = int(input("How many numbers would you like? "))
random.shuffle(letters)#embaralha a lista
password=""
password_final=""
for i in range(0,size_letters):
    a=random.randint(0,size_letters)
    password+=(letters[a])
for i in range(0,size_symbols):
    b=random.randint(0,size_symbols)
    password+=(symbols[b])
for i in range(0,size_numbers):
    c=random.randint(0,size_numbers)
    password+=(numbers[c])
size = size_letters+size_numbers+size_symbols
for i in range(0,size):
    d = random.randint(0,size-1)
    password_final+=password[d]
print(f"here is your password: {password_final}.")
