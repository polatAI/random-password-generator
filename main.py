# Developer: Seyfullah Polat
# Date: 10/07/2023
# Project: Random Password Generator
# Language: Python

import random
import string
import pyperclip

def generate_password(lenght,include_uppercase,include_lowercase,include_numbers,include_special_chars):

    chars = ""

    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation
    
    if len(chars) == 0:
        print("You must select at least one character type.")
        return None
    
    password = "".join(random.choice(chars) for _ in range(lenght))
    return password


def main():

    lenght = int(input("Enter password lenght: "))
    include_uppercase = input("Include uppercase letter? (Yes/No): ").lower() == "yes"
    include_lowercase = input("Include lowercase letter? (Yes/No): ").lower() == "yes"
    include_numbers = input("Include numbers (Yes/No): ").lower() == "yes"
    include_special_chars = input("Include special characters (Yes/No): ").lower() == "yes"

    password = generate_password(lenght,include_uppercase,include_lowercase,include_numbers,include_special_chars)

    if password:
        print(f"Your password is {password}")
        
        copy_to_clipboard = input("Do you want to copy the password (Yes/No): ").lower() == "yes"

        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard.")


if __name__ == "__main__":
    main()