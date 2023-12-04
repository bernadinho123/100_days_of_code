alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
size = len(alphabet)

def encrypt(text,shift):
    new_word = ""
    for i in text:
        x=alphabet.index(i)
        if (x+shift)>=size:
            new_word += alphabet[shift -1]
        else:
            new_word += alphabet[x+shift]
    print(f" The encoded text is {new_word}")

def decrypt(text,shift):
    new_word = ""
    for i in text:
        x=alphabet.index(i)
        new_word += alphabet[x-shift]
    print(f" The decoded text is {new_word}")


if direction == " encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)

