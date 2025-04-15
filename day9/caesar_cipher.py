alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("TYpe the shift number:\n"))


def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position= position+shift_amount
        if(new_position>25):
            new_position=new_position%25

            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            new_letter=alphabet[new_position]
            cipher_text+=new_letter

    print(f"the encoded text is {cipher_text}")

encrypt(text,shift)
cipher_text=input("To decrypt: ")


def decrypt(cipher_text, shift_amount):
    converted_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position+(25-shift_amount)
        if(new_position>=25):
            new_position=new_position%25
            new_letter=alphabet[new_position]
            converted_text+=new_letter
        else:
            new_letter=alphabet[new_position]
            converted_text+=new_letter
    print(f"the decode text is {converted_text}")
    
decrypt(cipher_text,shift)

