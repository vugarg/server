from http import client, server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)

client, address = server.accept()

while True:
    data = input("Enter message or q to quit: ").encode('utf-8')
    decodedData = data.decode('utf-8')
    client.send(data)
    if decodedData == 'q':
        break

client.close()
server.close()


    
    