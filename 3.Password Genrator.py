# TASK-3-Password Genrator
'''
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
'''

import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    password = []
    
    # User selection character types to the pool
    if use_uppercase:
        character_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        character_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        character_pool += string.digits
        password.append(random.choice(string.digits))
    if use_special:
        character_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if not character_pool:
        raise ValueError("No character types selected. At least one type must be chosen.")
    
    # Ensureing the password is of the desired length
    while len(password) < length:
        password.append(random.choice(character_pool))

    # Shuffling the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def get_user_input():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return None

        print("Select the character types to include in the password:")
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        return length, use_uppercase, use_lowercase, use_digits, use_special
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def main():
    user_input = get_user_input()
    if user_input:
        length, use_uppercase, use_lowercase, use_digits, use_special = user_input
        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
