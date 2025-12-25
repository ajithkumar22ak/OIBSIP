import random
import string

print("🔐 RANDOM PASSWORD GENERATOR 🤐")
try:
    length = int(input("📏 Boss please enter your password length: "))

    if length <= 0:
        print("❌ Boss password length must be greater than 0 😤")
    else:
        print("\n🎯 Boss choose your character types:")

        use_letters = input("🔤 Include letters? (yes/no): ").strip().lower()
        use_numbers = input("🔢 Include numbers? (yes/no): ").strip().lower()
        use_symbols = input("💥 Include symbols? (yes/no): ").strip().lower()

        characters = ""
        password = []

        if use_letters == "yes":
            characters += string.ascii_letters
            password.append(random.choice(string.ascii_letters))
            print("✅ Letters added 🔤")

        if use_numbers == "yes":
            characters += string.digits
            password.append(random.choice(string.digits))
            print("✅ Numbers added 🔢")

        if use_symbols == "yes":
            characters += string.punctuation
            password.append(random.choice(string.punctuation))
            print("✅ Symbols added 💥")

        if not characters:
            print("😒 Boss please select at least ONE character type!")
        elif length < len(password):
            print("⚠️ Boss password length is too small for selected options!")
        else:
            remaining_length = length - len(password)

            for _ in range(remaining_length):
                password.append(random.choice(characters))

            random.shuffle(password)

            print("\n🎉 Password generated successfully!")
            print("🔑 Boss your secure password is 👉", "".join(password))
            print("😎 Use it safely boss!")

except ValueError:
    print("🚫 Sorry boss!! Please enter numbers only 😊")
