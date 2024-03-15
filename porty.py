import socket
import time

def banner_grab(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        s.settimeout(3)
        # Try to connect to the host and port
        s.connect((host, port))
        # If connection successful, the port is open
        banner = s.recv(1024).decode().strip()
        return port, "open", banner
    except Exception as e:
        # If connection fails, the port is closed or unreachable
        return port, "closed/unreachable", str(e)
    finally:
        # Close the socket
        s.close()

def check_ports(host, start_port, end_port):
    print("Scanning for ports... ", end="", flush=True)
    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

    open_ports = []
    for port in range(start_port, end_port + 1):
        port, status, banner = banner_grab(host, port)
        if status == "open":
            open_ports.append((port, banner))
    
    if open_ports:
        print("Open ports:")
        for port, banner in open_ports:
            print(f"Port {port}: {banner}")
    else:
        print(f"No open ports found in range {start_port}-{end_port} on {host}")

if __name__ == "__main__":
    # Prompt the user for the host/IP address, start port, and end port
    host = input("Enter the host/IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    # Call the function to check the ports
    check_ports(host, start_port, end_port)
