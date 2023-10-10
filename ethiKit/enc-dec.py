from cryptography.fernet import Fernet

def generate_key():
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

choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ")

if choice.lower() == 'e':
    key = generate_key()
    print("Encryption key:", key.decode())
    file_path = input("Enter the path of the file you want to encrypt: ")
    encrypt_file(file_path, key)
    print("File encrypted successfully.")
elif choice.lower() == 'd':
    key = input("Enter the encryption key: ").encode()
    encrypted_file_path = input("Enter the path of the encrypted file: ")
    decrypt_file(encrypted_file_path, key)
    print("File decrypted successfully.")
else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
