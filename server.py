import socket
from _thread import *

host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print('waiting for a connection.')
def clientHandle():
	#conn, addr=s.accept()
	print('connected by',addr)
	while True:
	    data=conn.recv(1024)
	    
	    reply='Server out:' +data.decode('uft-8')
	    if not data:break
	    conn.sendall(str.encode(reply))
	    #print(data)
	conn.close()


while True:
	conn, addr=s.accept()
	print('connected to:'+addr[0]+':'+str(addr[1]))
	start_new_thread(clientHandle,(conn,))


	t=Thread(target=clientHandle)
	t.start()
s.close()


