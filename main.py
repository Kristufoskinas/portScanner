import pythonping, socket
from concurrent.futures import ThreadPoolExecutor

def get_ip():
    return input("Enter IP address: ")

def ping(ip):
    response = pythonping.ping(ip, count=10)
    for resp in response:
        if resp.success:
            return True
    return False

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.3)

    result = s.connect_ex((ip, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

if __name__ == "__main__":
    ip = get_ip()
    ping_alive = ping(ip)
    if not ping_alive:
        choice = input("No pings were returned. Do you want to continue anyway? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting.")
            exit()        

    with ThreadPoolExecutor(max_workers = 200) as executor:
        for port in range(1, 65535): # 1025 - for basic ports OR 65535 - for ALL ports
            executor.submit(scan_port, ip, port)