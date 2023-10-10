from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(encrypted_file_path[:-4], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
# Encrypt a file
encrypt_file("example.txt")

# Decrypt the encrypted file
decrypt_file("example.txt.enc")
