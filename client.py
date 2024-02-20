# encoding: utf-8
'''
@author: binky
@file: client.py
@time: 2023/7/27 22:55
@desc:
'''

import socket

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))

    print("服务器说：", s.recv(1024).decode())
    s.sendall('你好，我是 Python 客户端'.encode())

    s.close()

if __name__ == "__main__":
    start_client()