import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8090))
sock.listen(3)

print("服务器已经启动...")
while 1:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data:", data)
    # conn.send(b"HTTP/1.1 200 ok\r\n\r\n<h1>welcome to JD</h1><p>MAC Iphone YinXiang</p><img src='https://img1.baidu.com/it/u=2693733305,4035903587&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=1200'>")
    # conn.send("HTTP/1.1 200 ok\r\n\r\nwelcome to JD:MAC Iphone YinXiang".encode())
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n{"goods":["MAC","Iphone"]}')

    conn.close()
