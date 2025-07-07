import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    charset = list(string.ascii_lowercase)
    
    if use_upper:
        charset += list(string.ascii_uppercase)
    if use_digits:
        charset += list(string.digits)
    if use_symbols:
        charset += list("!@#$%^&*()-_")

    if not charset:
        return "No character types selected!"

    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    print("Welcome to your personal Password Genie!")
    try:
        length = int(input("Desired password length: "))
    except ValueError:
        print("That's not a number, bestie.")
        return

    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, digits, symbols)
    print(f"Your secure password: {password}")

if __name__== "__main__":
    main()
