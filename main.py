import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+=-[]{}|;:,.<>?'
    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    while True:
        if length < 4:
            print("Error: Password length must be at least 4 characters.")
            return None

        password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)
        password += ''.join(random.choice(all_characters) for _ in range(length - 4))

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password

while True:
    try:
        print(" It has to be greater or equals to 4")
        password_length = int(input("Enter the desired password length:"))
        password = generate_password(password_length)
        
        if password:
            print(f"Generated Password: {password}")
        
            another = input("Do you want to generate another password (yes/no): ")
            if another == 'yes':
                continue
            elif another == 'no':
                print("Thanks for using Muhais's Password Generator")
                break  
            else:
                print("Invalid input. Exiting the loop.")
                break
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for password length.")
        
       
       