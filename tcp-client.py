import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port))

    filename = input("Input filename:")
        
    fi = open(filename,"r")
    data = fi.read()

    sock.send(str(data).encode())

    data = fi.read()

    fi.close()        