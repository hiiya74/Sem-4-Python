import socket 
host= socket.gethostname()
port=5100
udp_client=socket.socket(type=socket.SOCK_DGRAM)
udp_sever.bind((host,port))
while True:
    print('waiting for message')
    data,addr=udp_server.recvfrom(1024)
    print('received',data.decode(),'from',addr)
    msg=input('Enter msg:')
    udp_server.sendto(msg.encode(),addr)
udp_server.close()
