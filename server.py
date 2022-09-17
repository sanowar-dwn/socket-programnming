import socket

# always specify the ip address

HOST = '192.168.199.1'

PORT = 12344
initial = 0
ticket_id = 12345

# defining the server and the type of socket, sock_stream means that it is a tcp socket,
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now we need to bind the server to a host and the port
server.bind((HOST,PORT))

# keep listening, at max 5 connections,
# if more than 5 conections are waiting then we reject
server.listen(5)


# this while loop is never ending!
while True:
    # we communicate using the communication socket
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    # specifying the number of bytes to receive
    # you need to be able to decode the messages in order to read the messages
    # has the ability to send 1024 bytes
    message = communication_socket.recv(1024).decode('utf-8')
    message1 = int(message)
    message_list = []
    for i in range(1, message1):
        if message1 % i == 0:
            message_list.append(i)
        else:
            pass

    print(f"Your ticket id is {ticket_id}")
    ticket_id = ticket_id + 13
    initial = initial + 1
    communication_socket.send(f"your results are {message_list}".encode('utf-8'))
    communication_socket.close()
    print(f"total number of connections {initial}")
    print(f"Connection with {address} ended")



















