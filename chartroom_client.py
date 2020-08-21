#客户端程序
"""
    chart room客户端
    发送请求  接收结果
"""
from socket import socket

# 需要连接的主机地址,此处为本机测试地址
HOST = "127.0.0.1"
POST = 8000
ADDR = (HOST,POST)

sock = socket()
sock.connect(ADDR)

# 首先向服务端发送个人名称
def talk():
    pass


while True:
    msg = input("请输入名字:")
    msg = "NAME " + msg
    sock.send(msg.encode())
    response = sock.recv(1024).decode()
    # print(response)
    if response == "ok":
        talk()
    elif response == "Fail":
        print("存在重复的名称:")
        continue