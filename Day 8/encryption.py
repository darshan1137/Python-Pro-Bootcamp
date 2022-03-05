alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(text,shift): 
    cipher_test = ""
    for letter in text:
        pos = alphabet.index(letter)
        new_pos = pos +shift
        if new_pos > 26: 
            new_pos -= 26 
        new_letter = alphabet[new_pos]
        cipher_test += new_letter
    print (cipher_test)

def decrypt(text, shift):
    cipher_test =""
    for leter in text:
        pos = alphabet.index(leter)
        new_pos = pos - shift
        if new_pos < 1:
            new_pos += 26
        new_letter = alphabet[new_pos]
        cipher_test += new_letter
    print(cipher_test)

end =False
while end != True:
    direction = input("Type 'encode' for encryption or exit for Quiting program, and 'decode' for decryption: \n")
    if direction == "encode":
        text = input("Type your Message: \n").lower()
        shift = int(input("Enter the Shift Value\n"))
        encrypt(text,shift)

    elif direction == "exit":
        print("Thank you ! Visit again")
        end = True

    elif direction == "decode":
        text = input("Type your Message: \n").lower()
        shift = int(input("Enter the Shift Value\n"))
        decrypt(text,shift)

    else:
        print("Wrong Direction")
