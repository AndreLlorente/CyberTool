import socket
import ipaddress

def scan_ports(target_ip, port_range):
    open_ports = []  # List to store open ports

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout value for each port
        result = sock.connect_ex((str(target_ip), port))
        if result == 0:
            open_ports.append(port)  # Add open port to the list
        sock.close()

    if open_ports:
        print(f"\nOpen ports for {target_ip}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"No open ports found for {target_ip}")

def port_scanner_function():
    print("What do you wish to analyze using the VirusTotal Platform?")
    print("1. Scan a single IP ")
    print("2. Scan a Network")
    choice = input("-> ")

    if choice == '1':
        target_ip = input("Enter the IP address to scan: ")
        target_ips = [target_ip]
    elif choice == '2':
        network = input("Enter the network address to scan (e.g., 192.168.1.0/24): ")
        target_ips = [str(ip) for ip in ipaddress.IPv4Network(network)]
    else:
        print("Invalid choice!")
        return

    port_option = input("Enter '1' to scan a specified port or '2' to scan a port range: ")

    if port_option == '1':
        target_port = int(input("Enter the port to scan: "))
        port_range = [target_port]
    elif port_option == '2':
        start_port = int(input("Enter the start port of the range: "))
        end_port = int(input("Enter the end port of the range: "))
        port_range = range(start_port, end_port + 1)
    else:
        print("Invalid choice!")
        return

    for ip in target_ips:
        scan_ports(ip, port_range)

if __name__ == "__main__":
    port_scanner_function()