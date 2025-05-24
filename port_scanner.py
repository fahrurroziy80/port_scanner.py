
import socket
import argparse
from datetime import datetime

def scan_ports(target, ports):
    print(f"\n[+] Scanning target: {target}")
    print(f"[+] Time started: {datetime.now()}\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", help="Target host to scan (e.g. 192.168.1.1 or google.com)")
    parser.add_argument(
        "-p", "--ports", nargs="+", type=int,
        help="List of ports to scan (e.g. -p 22 80 443)", required=True
    )

    args = parser.parse_args()
    try:
        ip = socket.gethostbyname(args.host)
        scan_ports(ip, args.ports)
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\n[-] Scan cancelled by user.")
