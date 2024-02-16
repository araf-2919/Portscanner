import socket
def portscan(ip):
    print(f'\nStarting a scan on {ip}')
    openPorts = 0 
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f'Port:{port}')
                openPorts +=1
        except socket.error:
            pass
        finally:
            s.close()
portscan('your ip address')
