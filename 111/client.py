import socket

#better to use the wireless LAN adapter wifi IP
#this is your device ip address
HOST = #Enter your ip here#

PORT = 9090

#making a client socket and defining the type of socket and the type of data receiving
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))


client.send("Hello World\n".encode(('utf-8')))

#print whatever you receive form the server
print(client.recv(1024).decode('utf-8'))
