import socket

serv = socket.socket()

port = 12345
serv.bind(('', port))

serv.listen(5)

conn, addr = serv.accept()

while True:
    data = conn.recv(1024)
    print(data)
    
    if not data:
        break
    val = str(input("Enter msg:"))
    conn.send(val.encode())

conn.close()