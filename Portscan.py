import socket

def check_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            s.settimeout(3)
            # Try to connect to the host and port
            s.connect((host, port))
            # If connection successful, the port is open
            print(f"Port {port} is open on {host}")
            # Attempt banner grabbing
            banner = s.recv(1024)
            if banner:
                print(f"Banner for port {port}: {banner.decode().strip()}")
        except Exception as e:
            # If connection fails, the port is closed or unreachable
            print(f"Port {port} is closed or unreachable on {host}: {e}")
        finally:
            # Close the socket
            s.close()

if __name__ == "__main__":
    # Prompt the user for the host/IP address, start port, and end port
    host = input("Enter the host/IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    # Call the function to check the ports
    check_ports(host, start_port, end_port)
