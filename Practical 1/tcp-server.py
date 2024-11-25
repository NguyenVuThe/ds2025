import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    clients = 5

    sket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sket.bind((host, port)) 
    sket.listen(clients) 

    print("Initiating clients")

    client_socket, client_address = sket.accept()
    
    data = client_socket.recv(1024).decode()

    filename = 'output.txt'

    fo = open(filename, 'w')

    fo.write(data)
    print('Received successfully! New filename is:', filename) 
    client_socket.close()
        