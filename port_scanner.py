#In this lab, we are creatinga port scanner. We are going to determine if the first 500 ports are open or closed.
 
from socket import *
import time
 
def port_scanner(port_num):

    IP_ADDRESS = ('127.0.0.1')
    
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((IP_ADDRESS,port_num))
        print(f"Port {port_num}: OPEN")
        sock.close()

    except Exception as e:
        pass

def main():
    print("Welcome to Port Scanner!")
    print("The address scanned today is 127.0.0.1")
    print("__________________________")

    begin = time.time()
    for port in range(0,500):
        port_scanner(port)
    finish = time.time()

    completion = finish - begin
    print(completion)
 
if __name__ == '__main__':

    main()

