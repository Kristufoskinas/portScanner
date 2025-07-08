import pythonping, socket
from concurrent.futures import ThreadPoolExecutor

ip = input("Enter IP address: ")
ping = pythonping.ping(ip, count=10)
print(ping)

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.3)

    result = s.connect_ex((ip, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

with ThreadPoolExecutor(max_workers = 200) as executor:
    for port in range(1, 1025): # DEFINE THE RANGE 1025 or 65535 (until 65535 for all ports)
        executor.submit(scan_port, ip, port)
