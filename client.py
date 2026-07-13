import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "10.76.166.212"   # Replace with your server's IPv4 address
port = 5000

client.connect((server_ip, port))

# Client user input
message = input("Enter message: ")
client.send(message.encode())

reply = client.recv(1024).decode()
print("Server:", reply)

client.close()