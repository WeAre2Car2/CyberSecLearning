import socket
from concurrent.futures import ThreadPoolExecutor

server_ip = "127.0.0.1"
open_ports = []


def load_ports_from_file(file_path="ports.txt"):
    port_list = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                port = int(line)

                if 1 <= port <= 65535:
                    port_list.append(port)

            except ValueError:
                continue

    return port_list



def grab_regular_banner(client):
    try:
        client.settimeout(1)
        banner = client.recv(1024)

        if banner:
            return banner.decode("utf-8", errors="ignore").strip()

    except socket.timeout:
        pass
    except Exception:
        pass

    return None


def grab_http_banner(client, host):
    try:
        request = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"User-Agent: Python-Port-Scanner\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        )

        client.sendall(request.encode())
        response = client.recv(4096)

        if response:
            return response.decode("utf-8", errors="ignore").strip()

    except socket.timeout:
        pass
    except Exception:
        pass

    return None


def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(2)

            result = client.connect_ex((server_ip, port))

            if result == 0:
                print(f"\n{port}/tcp open")

                banner = grab_regular_banner(client)

                if banner:
                    print("Regular banner:")
                    print(banner)
                else:
                    banner = grab_http_banner(client, server_ip)

                    if banner:
                        print("HTTP response:")
                        print(banner)
                    else:
                        print("No banner received")

                return port

    except Exception as e:
        print(f"Error scanning port {port}: {e}")

    return None

ports = load_ports_from_file()

with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(scan_port, ports)

    for port in results:
        if port is not None:
            open_ports.append(port)

print("\nOpen ports:")
for port in open_ports:
    print(f"{port}/tcp open")
