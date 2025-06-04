import socket
host = socket.gethostname()
port = 4701
udp_client = socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg = input('enter msg')
    if not msg:
        break
    udp_client.sendto(msg.encode(),(host,port))
    print('ready toooo')
    data,addr = udp_client.recvfrom(1024)
    if not data:
        break
    print('received',data.decode())
udp_client.close()
