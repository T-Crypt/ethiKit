import socket
import threading
from queue import Queue

target = input("Enter the IP address of the target: ")

# Create a queue to store open ports
open_ports = Queue()

def scan_port(port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        socket.setdefaulttimeout(1)
        # Attempt to connect to the target IP address and port
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.put(port)
        # Close the socket
        sock.close()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"Error: {e}")


def banner_grabbing(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((target, port))
            banner = sock.recv(1024).decode().strip()
            return banner
    except (socket.timeout, ConnectionRefusedError):
        return None

def scan_ports():
    for port in range(1, 1025):  # Scanning common ports
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

def get_open_ports():
    scan_ports()
    thread_count = 0
    for t in threading.enumerate():
        if t != threading.current_thread():
            t.join()
            thread_count += 1
    print(f"Scanning completed. {open_ports.qsize()} open ports found:")
    while not open_ports.empty():
        port = open_ports.get()
        banner = banner_grabbing(port)
        print(f"Port {port} - Banner: {banner}")

get_open_ports()
