import string
from time import sleep

alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"


def encrypt():
    print("Welcome to Caesar Cipher Encryption.\n")
    message = input("Type a message you would like to encrypt: ").lower()
    print()
    key = int(input("Enter your key: "))

    encrypted_message = ""

    for c in message:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c

    print("\nEncrypting your message...\n")
    sleep(2)  # give an appearance of doing something complicated
    print("Stand by, almost finished...\n")
    sleep(2)  # more of the same
    print("Your encrypted message is:\n")
    print(encrypted_message)


encrypt()