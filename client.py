import socket

HOST = '192.168.199.1'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send('Hello World!....'.encode('utf-8'))
client.send('Hello World!....'.encode('utf-8'))
client.send('Hello World!....'.encode('utf-8'))
message = client.recv(1024).decode('utf-8')

print(f'message received from the server was {message}')

client.close()