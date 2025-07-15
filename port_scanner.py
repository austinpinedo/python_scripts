#In this lab, we are creatinga port scanner. We are going to determine if the first 500 ports are open or closed.
 
from socket import *
import ipaddress
import time
 
def port_scanner(IP_ADDRESS, port_num):

    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((IP_ADDRESS,port_num))
        print(f"Port {port_num}: OPEN")
        sock.close()

    except Exception as e:
        print(f"Port {port_num}: CLOSED ({e})")

def main():
    print("Welcome to Port Scanner!")
    try: 
        IP_ADDRESS = input("Enter an IP Address:")
        ipaddress.ip_address(IP_ADDRESS)
    except ValueError:
        print("Invalid IP Address.")
        return
    
    print(f"The address scanned today is {IP_ADDRESS}")
    print("__________________________")

    begin = time.time()
    for port in range(0,500):
        port_scanner(IP_ADDRESS, port)
    finish = time.time()

    completion = finish - begin
    print(completion)
 
if __name__ == '__main__':

    main()

