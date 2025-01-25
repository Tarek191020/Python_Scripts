import os
import socket

subnet = input("Enter first three octect (e.g., 192.168.1): ")
first_ip = int(input("Enter first IP (last octet): "))
last_ip = int(input("Enter last IP (last octet): "))

first_port = int(input("Enter first port: "))
last_port = int(input("Enter last port: "))

ip_on = []
ports_on = {} 

file_path = r"F:\MCS\07-scripting\scan_result.txt"

# Function to ping an IP
def ping(ip):
    response = os.system(f"ping {ip} -n 1 -w 1 > nul 2>&1")
    if response == 0:
        return True

# Function to scan a port
def scan_port(ip, port):
    result = False
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conn.settimeout(1)
    response = socket_conn.connect_ex((ip,port))
    if response == 0:
        result = True
    else:
        result = False
    socket_conn.close()
    return result
     
# Ping each IP in the range
print(f"scanning online IPs in range {subnet}.{first_ip}-{subnet}.{last_ip}...")
for i in range(first_ip, last_ip + 1):
    ip = f"{subnet}.{i}"
    if ping(ip):
        ip_on.append(ip)

# Write online IPs to file
with open(file_path, 'w') as file:
    file.write("Online IPs:\n")
    for ip in ip_on:
        file.write(f"{ip}\n")
    print("Online IPs:")
    print(ip_on)

# Scan ports for each online IP
for ip in ip_on:
    print(f"\nScanning ports for {ip}...")
    ports_on[ip] = []  # Initialize empty list for this IP
    for port in range(first_port, last_port + 1):
        if scan_port(ip, port):
            ports_on[ip].append(port)

# Write open ports to file
with open(file_path,"a") as file:
    print("\nOpen Ports:")
    file.write("\nOpen Ports:\n")
    for ip, ports in ports_on.items():
        if ports:
            ports_str = ", ".join(map(str, ports))
            print(f"{ip}: {ports_str}")
            file.write(f"{ip}: {ports_str}\n")
        else:
            print(f"{ip}: No open ports in the range {first_port}-{last_port}")
            file.write(f"{ip}: No open ports in the range {first_port}-{last_port}\n")

# Print results
print("\nScan results saved to:", file_path)
