import socket

#always specify the ip address
HOST = #Enter your ip here#

PORT = 9090


# defining the server and the type of socket, sock_stream means that it is a tcp socket,
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#now we need to bind the server to a host and the port
server.bind((HOST,PORT))

#keep listening, at max 5 connections,
#if more than 5 conections are waiting then we reject
server.listen(5)


#this while loop is never ending!
while True:
    # we communicate using the communication socket
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    #specifying the number of bytes to receive
    #you need to be able to decode the messages in order to read the messages
    # has the ability to send 1024 bytes
    message = communication_socket.recv(1024).decode('utf-8')

    print(f"Message from the client is {message}")

    communication_socket.send(f"Got your message, Thank You!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended")


