# -*- coding: utf-8 -*-
import socket
import concurrent.futures
import json
import logging
import time

from tools.log import Log
from net import mgrnet
import defines

BUFFSIZE = 4096


def handle_client(client_socket):
    # 服务端接收消息
    total_data = ""
    while True:
        # 将收到的数据拼接起来
        data = client_socket.recv(BUFFSIZE).decode()
        if "::end" in data:
            total_data += data.replace("::end", "")
            break
        total_data += data
    request = total_data
    print("接受的原始消息====", request)
    dData = json.loads(request)
    mgrnet.HandOut(client_socket, dData)


def thread_pool_callback(worker):
    logging.info("called thread pool executor callback function")
    worker_exception = worker.exception()
    if worker_exception:
        logging.exception("Worker return exception: {}".format(worker_exception))


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((defines.HOST, defines.PORT))
    server_socket.listen(5)

    Log("Server started and listening for clients to connect...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            client_socket, address = server_socket.accept()
            Log(f"Connection from: {str(address)}")
            thread_pool_exc = executor.submit(handle_client, client_socket)
            thread_pool_exc.add_done_callback(thread_pool_callback)


if __name__ == "__main__":
    server_program()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = "Hello, client!"
    client_socket, address = server_socket.accept()
    client_socket.sendall(message.encode())
    print("已发送消息给客户端")

    # 模拟一些处理时间
    time.sleep(1)

    message = "Hello2, client!"
    client_socket, address = server_socket.accept()
    client_socket.sendall(message.encode())

