import socket

cli = socket.socket()
port = 12345
cli.connect(('127.0.0.1', port))
val = str(input("Enter msg:"))

while val != "Bye":
    cli.send(val.encode())
    print (cli.recv(1024))
    val = str(input("Enter msg:"))

cli.close()