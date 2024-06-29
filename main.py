import random
import string

def generate_pass(length=12):
    #Define character to use in the password
    characters= string.ascii_letters + string.digits + string.punctuation

    #Generate password by randomly selecting character 
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    password_length =int(input("enter the desired password length: "))

    if password_length < 1:
        print("Password length must be at least 1 character .")
    else:
        generate_pass = generate_pass(password_length)
        print("Generate Password:", generate_pass)

