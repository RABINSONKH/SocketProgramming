import socket

serv = socket.socket() 
port = 12345 
addr = '127.0.0.1' 
serv.bind((addr, port)) 

serv.listen(5) 

while True:
    conn, addr = serv.accept()
    conn.send(b'Thank you for connecting!')
    conn.close() 
    break 