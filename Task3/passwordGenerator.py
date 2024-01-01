import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    if complexity == '1':
        characters = lowercase_letters
    elif complexity == '2':
        characters = lowercase_letters + uppercase_letters
    elif complexity == '3':
        characters = lowercase_letters + uppercase_letters + digits
    elif complexity == '4':
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        print("Invalid complexity level.")
        return None

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Get user input for password length and complexity
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (1-4):\n"
                       "1. Lowercase Letters\n"
                       "2. Lowercase and Uppercase Letters\n"
                       "3. Alphanumeric (Letters and Digits)\n"
                       "4. Alphanumeric and Special Characters\n")

    # Generate and display the password
    password = generate_password(length, complexity)
    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
