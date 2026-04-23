import random
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
