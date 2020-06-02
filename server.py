import json
import socket
import threading

from datetime import datetime

print('等待连接ing....')
host_port = ('127.0.0.1', 8888)

s = socket.socket()
s.bind(host_port)
s.listen(1)

conn, addr = s.accept()
true = True
print(f'来自: {addr} 的连接')


def recv(connection):
    global true

    while true:
        data = json.loads(connection.recv(1024).decode())
        if data == 'quit':
            true = False
        print(f'来自 {addr} : {data[1]} 的消息 -> ', data[0])


thread1 = threading.Thread(target=recv, args=(conn, ))
thread1.start()

while true:
    msg = input()
    msg = json.dumps([msg, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    conn.send(msg.encode())
    if msg == 'quit':
        true = False

s.close()
