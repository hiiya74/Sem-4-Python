import socket
host=socket.gethostname()
port=4701
server_socket=socket.socket(type=socket.SOCK_DGRAM)
server_socket.bind((host,port))
print(f"UDP Server Listening on {host}:{port}")
while True:
    data,addr=server_socket.recvfrom(1024)
    try:
        number=int(data.decode())
        squared=number**2
        response=str(squared)
    except ValueError:
        response="invalid"
    server_socket.sendto(response.encode(),addr)
server_soclet.close()
