import socket
from concurrent.futures import ThreadPoolExecutor

server_ip = "127.0.0.1"
open_ports = []

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(1)

            if client.connect_ex((server_ip, port)) == 0:
                return port
    except Exception:
        pass

    return None


with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(scan_port, range(65536))

for port in results:
    if port is not None:
        open_ports.append(port)
        print(f"{port}/tcp open")

print("Open ports:", sorted(open_ports))