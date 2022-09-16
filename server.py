import socket
HOST = '192.168.199.1'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

while True:
    communictaion_socket, address = server.accept()
    print(f'connected to {address}')
    message = communictaion_socket.recv(1024).decode('utf-8')
    print(f'message from the client {message}')
    communictaion_socket.send('got your message'.encode('utf-8'))
    communictaion_socket.close()

    print(f"connection with {address} has ended")


