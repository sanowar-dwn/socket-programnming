import socket

# better to use the wireless LAN adapter Wi-Fi IP
# this is your device ip address
HOST = "192.168.199.1"

PORT = 12344

# making a client socket and defining the type of socket and the type of data receiving
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))
number = '12'

client.send(number.encode(('utf-8')))

# print whatever you receive form the server
print(client.recv(1024).decode('utf-8'))
