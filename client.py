from tkinter import *

import socket
host='127.0.0.1'#socket.gethostname()
port=12345
master=Tk()

def enter():
    l=Label(master,text=e1.get()).grid(row=1)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    #s.sendall(b'Hello, World\n')
    s.sendall(e1.get().encode())
    data=s.recv(1024)
    s.close()
    print('Received',repr(data))

e1=Entry(master)
e1.grid(row=3,columnspan=5)
l1=Label(master,text=" ").grid(row=1)
b1=Button(master,text='enter',command=enter).grid(row=2,column=0)

while True:
    master.update()
