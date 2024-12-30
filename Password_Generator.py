import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def save_password_to_file(password, filename="generated_password.txt"):
    with open(filename, "w") as file:
        file.write(password)
    print(f"Password saved to {filename}")

password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated Password: {password}")

save_choice = input("Do you want to save this password to a file? (y/n): ").lower()

if save_choice == 'y':
    save_password_to_file(password)
else:
    print("Password not saved.")
