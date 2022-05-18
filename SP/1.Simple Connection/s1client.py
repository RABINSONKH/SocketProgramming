import socket

cli = socket.socket() # socket object creation
port = 12345 # need to learn this port number from server

# client needs to know the following parameters already
cli.connect(('127.0.0.1', port)) # connection request
print (cli.recv(1024)) # capture any message sent from server
cli.close() # close the connection

