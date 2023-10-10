import secrets
import string

def generate_secure_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secure_password

# Example usage
password_length = 16  # You can adjust the length as per your requirement
secure_password = generate_secure_password(password_length)
print("Secure Password:", secure_password)
