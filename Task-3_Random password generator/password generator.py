import random
print("🔐 RANDOM PASSWORD GENERATOR 🔐")
length = int(input("📏 Enter password length: "))
if length <= 0:
    print("❌ Password length must be greater than 0!")
    exit()
use_letters = input("🔤 Include letters? (yes/no): ").strip().lower()
use_numbers = input("🔢 Include numbers? (yes/no): ").strip().lower()
use_symbols = input("🔣 Include symbols? (yes/no): ").strip().lower()
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
characters = ""
password_list = []
if use_letters == "yes":
    characters += letters
    password_list.append(letters[random.randint(0, len(letters)-1)])
if use_numbers == "yes":
    characters += numbers
    password_list.append(numbers[random.randint(0, len(numbers)-1)])
if use_symbols == "yes":
    characters += symbols
    password_list.append(symbols[random.randint(0, len(symbols)-1)])
if characters == "":
    print("⚠️ Please select at least one character type!")
    exit()
while len(password_list) < length:
    index = random.randint(0, len(characters)-1)
    password_list.append(characters[index])
for i in range(len(password_list)):
    j = random.randint(0, len(password_list)-1)
    password_list[i], password_list[j] = password_list[j], password_list[i]
password = ""
for ch in password_list:
    password += ch
print("\n✅ Your Generated Password is:",password)


