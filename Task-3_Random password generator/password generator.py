import random
import string

print("RANDOM PASSWORD GENERATOR 🤐")

try:
    length = int(input("Boss please enter your password length: "))

    if length <= 0:
        print("Boss password length must be greater than 0.")
    else:
        print("Boss choose your character types:")

        use_letters = input("Include letters? (yes/no): ").strip().lower()
        use_numbers = input("Include numbers? (yes/no): ").strip().lower()
        use_symbols = input("Include symbols? (yes/no): ").strip().lower()

        characters = ""

        if use_letters == "yes":
            characters += string.ascii_letters
        if use_numbers == "yes":
            characters += string.digits
        if use_symbols == "yes":
            characters += string.punctuation

        if not characters:
            print("Boss please select at least one character type 😒!")
        else:
            password = "".join(random.choice(characters) for _ in range(length))
            print("\nBoss your generated password is:", password)

except ValueError:
    print("Sorry!! Please enter a valid numeric input 😊")
