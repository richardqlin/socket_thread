from socket import *
host='127.0.0.1'#socket.gethostname()
port=12345
s=socket()
s.connect((host,port))
s.send('hello world!')
s.close()