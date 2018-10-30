#Creating the server with localhost and port number 6969
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = socket.gethostname()
ip = socket.gethostbyname(name)
port = 6969
address = (ip, port)
server.bind(address)
server.listen(1)    #Listening only from one client at a time
connection_str = "Started listening on " + str(ip) + ":" + str(port)
print(connection_str)

#Infinite loop waiting for client to connect and send data
while (True):
    client, addr = server.accept()
    validation_str = "Got a connection from " + str(addr[0]) + ":" + str(addr[1])
    data_received = client.recv(port)
    receive_str = "Received: " + data_received.decode()
    print(receive_str)
    print("Giving Data back________________________________________________")
    data_sent = create_json()
    client.send(data_sent.encode())
    #if client send 'disconnect'
    if (data_received == b"disconnect"):
        client.close()
        break
