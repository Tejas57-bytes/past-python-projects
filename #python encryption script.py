#python encryption script

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
characters = list(characters)
keys = characters.copy()

random.shuffle(keys)

#encryption dictionary
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""
for char in plain_text:
    if char in characters:
        index = characters.index(char)
        cipher_text += keys[index]
    else:
        cipher_text += char  # Keep the character unchanged if not in the list
print("Encrypted text:", cipher_text)

#decryption dictionary
cipher_text = input("Enter the text to decrypt: ")
original_message = ""
decrypted_text = ""
for char in cipher_text:
    if char in keys:
        index = keys.index(char)
        decrypted_text += characters[index]
    else:
        decrypted_text += char  # Keep the character unchanged if not in the list
print("Decrypted text:", decrypted_text)