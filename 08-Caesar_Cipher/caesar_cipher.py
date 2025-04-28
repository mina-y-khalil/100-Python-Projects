alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount ):
    the_new_message = ""
    if direction == "encode":
        for letter in original_text:
            if letter in alphabet:
                the_original_index = alphabet.index(letter)
                the_new_index = (the_original_index + shift_amount) % 26
                letter = alphabet[the_new_index]
                the_new_message += letter
            else:
                the_new_message += letter
        print(f"Here is the encoded result: {the_new_message}")


    elif direction == "decode":
        for letter in original_text:
            if letter in alphabet:
                the_original_index = alphabet.index(letter)
                the_new_index = (the_original_index - shift_amount) % 26
                letter = alphabet[the_new_index]
                the_new_message += letter
            else:
                the_new_message += letter
        print(f"Here is the decoded result: {the_new_message}")
    else:
        print("Please enter a valid value")

encrypt(text,shift)