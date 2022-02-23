alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direct,plain_text,shift_amount):
    converted_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direct == 'encode':
                new_position = position + shift_amount
                if new_position > 25:
                    new_position = new_position - 26
            elif direct == 'decode':
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = new_position + 26
            converted_text += alphabet[new_position]
        else:
            converted_text += char
    print(f"The {direct}d text is {converted_text}")

import art
print(art.logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 25:
        shift = shift % 26

    caesar(direct=direction,plain_text=text,shift_amount=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")

