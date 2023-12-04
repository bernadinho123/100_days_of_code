from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def ceaser (text,shift,direction):
       
        if direction == "encode":
            new_word = ""
            for i in text:
                if i not in alphabet:
                    new_word+= i
                else:
                    x=alphabet.index(i)
                    a = x+shift
                    if (a)>=size:
                        while a >= size:
                            a -= size
                        new_word += alphabet[a]
                    else:
                        new_word += alphabet[a]
            print(f" The encoded text is {new_word}")
            
        else:
            new_word = ""
            for i in text:
                x=alphabet.index(i)
                new_word += alphabet[x-shift]
            print(f" The decoded text is {new_word}")
flag = True

while flag == True:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print(" u gotta wright encode or decode")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        size = len(alphabet)
        ceaser(text,shift,direction)
        y = input("Type 'yes' if you want to go again. Otherwise type 'no'. " )
        if y == 'no':
            flag = False
        

   


