import sys
import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1',8888)
try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error,msg:
	print 'create socket failure .error code:' + str(msg[0]) + "Message:"+msg[1]
	sys.exit()
print 'socket created'
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
	server.bind(server_addr)
except socket.error,msg:
	print 'binding failure.error code:'+ str(msg[0])+'message:'+ msg[1]
	sys.exit()
print 'socket bind'
server.listen(5)
print 'socket listening'
while  True:
	client,client_addr = server.accept()
	print 'connected by',client_addr
	while  True:
		data = client.recv(BUF_SIZE)
		print data
		client.sendall(data)

server.close()