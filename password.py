import random
import string

def generate_username(length=8):
    """Generate a random username of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_password(length=12):
    """Generate a random password with letters, digits, and punctuation."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    username = generate_username()
    password = generate_password()
    print(f"Generated Username: {username}")
    print(f"Generated Password: {password}")
