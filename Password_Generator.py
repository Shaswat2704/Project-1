import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random choices from all categories
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to prevent predictable sequence
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    desired_length = int(input("Enter desired password length: "))
    print("Generated Password:", generate_password(desired_length))
