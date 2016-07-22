#------------------------------------------------------------------------------
#           Name: socket_test_server.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to create a socket,
#                 which will act as a simple server by listening to port 5000.
#
#                 Note, for anything to occur, you need to run this script
#                 simultaneously with the client-side script named,
#                 "socket_test_client.py".
#------------------------------------------------------------------------------

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

from threading import Thread 

import time
PORT_NUMBER = 9000

hostName = gethostbyname( '127.0.0.1' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port %d\n" % PORT_NUMBER)

print ("If you haven't started one or more client scripts already, do it now.\n")
def clientThread():

	while 1:
	    (data, addr) = mySocket.recvfrom( 50 ) # Just hard-code the data amount to read to 50
	    print ("Received packet from: " + str(addr) + ", " + str(data))
	    #mySocket.sendto((str(addr)+', '+str(data)).encode(), (hostName, PORT_NUMBER)) 
	    #time.sleep(1)


for i in range(2):
	Thread(target=clientThread).start()


