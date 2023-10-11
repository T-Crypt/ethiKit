import subprocess

def analyze_memory_dump(memory_dump_path):
    try:
        output = subprocess.check_output(["volatility", "-f", memory_dump_path, "imageinfo"], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode()}")

# Example usage
if __name__ == "__main__":
    memory_dump_path = input("Enter the path to the memory dump: ")
    analyze_memory_dump(memory_dump_path)
