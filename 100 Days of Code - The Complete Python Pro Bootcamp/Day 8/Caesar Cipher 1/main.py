from base64 import decode
from itertools import count

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
len_alphabet = len(alphabet)
def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index %= len_alphabet
        encrypted_text += alphabet[shifted_index]
    print(f"The encrypted text is :{encrypted_text}")
def decrypt(encrypted_text,shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        shifted_index = alphabet.index(letter) - shift_amount
        shifted_index %= len_alphabet
        decrypted_text+= alphabet[shifted_index]
    print(f"The decrypted text is : {decrypted_text}")

# A combined function for encoding and decoding
def caesar(text_input,shift_input,encode_decode):
    output_text = ""
    if encode_decode == 'encode':
        shift_input *=1
    if encode_decode == 'decode':
        shift_input *=-1
    for letter in text_input:
        shifted_index = alphabet.index(letter) +shift_input
        shifted_index %= len_alphabet
        output_text += alphabet[shifted_index]
    print(f"The {encode_decode} text is : {output_text}")

caesar(text_input= text,shift_input=shift,encode_decode=direction)
# if direction == 'encode':
#     encrypt(text,shift)
#
# if direction == 'decode':
#     decrypt(text,shift)