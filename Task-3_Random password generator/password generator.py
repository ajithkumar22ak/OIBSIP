import random
import string
print("RANDOM PASSWORD GENERATOR🤐")
try:
    length = int(input("Boss please enter your password length: "))
    if length <= 0:
        print("Boss password length must be greater than 0, so enter a valid length.")
        exit()
    print("Boss Choose your character types:")
    use_letters = input("Include letters? (yes/no): ").lower()
    use_numbers = input("Include numbers? (yes/no): ").lower()
    use_symbols = input("Include symbols? (yes/no): ").lower()
    characters = ""
    if use_letters == "yes":
        characters += string.ascii_letters
    if use_numbers == "yes":
        characters += string.digits
    if use_symbols == "yes":
        characters += string.punctuation
    if characters == "":
        print(" Boss Please will you select at least one character type😒!")
        exit()
    password = "".join(random.choice(characters) for _ in range(length))
    print("\nBoss your Generated Password is :", password)
except ValueError:
    print("sorry!! Please enter valid numeric input😊")
