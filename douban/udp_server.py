import socket

BUF_SIZE = 1024

server_addr = ('127.0.0.1',8888)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_addr)
while  True:
	print 'waiting for data'
	data,client_addr = server.recvfrom(BUF_SIZE)
	print 'connect by ',client_addr,'Receive Data',data
	server.sendto(data,client_addr)
server.close()

