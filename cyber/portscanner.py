import socket
from IPy import IP



#Scan Targets function
def scan(target, port_num):
    converted_ip = check_ip(target)
    print('\n' + '[-0 Scanning Target] ' + str(target))
    for port in range(1, port_num):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)



def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_address, port))
        try:
            banner = get_banner(sock)
            print('[+] OPen Port' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] OPen Port ' + str(port))
    except:
        pass

if __name__ == '__main__':
    targets = input('[+] Enter Target/s to scan, split multiple targets with , : ')
    port_num = int(input('Enter the number of ports , that you would like to scan:'))
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), port_num)
    else:
        scan(targets, port_num)


