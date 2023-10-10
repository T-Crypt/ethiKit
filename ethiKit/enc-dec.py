from cryptography.fernet import Fernet

def generate_key():
    # Generate a key for encryption
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    cipher_suite = Fernet(key)
    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(encrypted_file_path[:-4], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    user_key = input("Enter the encryption key (or press Enter to generate a new key): ").encode()
    if not user_key:
        user_key = generate_key()
        print("Generated Key:", user_key.decode())

    file_path = input("Enter the file path to encrypt: ")
    encrypt_file(file_path, user_key)

    encrypted_file_path = file_path + ".enc"
    print("File encrypted successfully.")

    decrypt_choice = input("Do you want to decrypt the file? (yes/no): ").lower()
    if decrypt_choice == "yes":
        decrypt_file(encrypted_file_path, user_key)
        print("File decrypted successfully.")
    else:
        print("Encryption key and encrypted file path required for decryption.")
