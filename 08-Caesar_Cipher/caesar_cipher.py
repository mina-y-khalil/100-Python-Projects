alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount, encode_or_decode ):
    the_new_message = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            the_original_index = alphabet.index(letter)
            the_new_index = (the_original_index + shift_amount) % len(alphabet)
            letter = alphabet[the_new_index]
            the_new_message += letter
        else:
            the_new_message += letter
    print(f"Here is the encoded result: {the_new_message}")

encrypt(original_text=text,shift_amount=shift, encode_or_decode=direction)