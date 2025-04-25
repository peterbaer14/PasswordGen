import random
import string

def generate_password(length):
    if length > 12:
        length = 12
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for _ in range(length))

def generate_multiple_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

print("Welcome to the password generator!")

while True:

    while True:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password (max 12): "))
        
        if password_length > 12:
            print("Password length must be 12 characters or fewer. Please try again.")
        else:
            break

    passwords = generate_multiple_passwords(num_passwords, password_length)
    print("Generated Passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}: {pwd}")

    again = input("Do you want to generate more passwords? (yes/no): ")
    if again != 'yes':
        print("Thank you for using the password generator!")
        break
