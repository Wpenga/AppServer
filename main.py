# -*- coding: utf-8 -*-
import socket
import concurrent.futures
import json
import logging
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
			client_sock, address = server_socket.accept()
			Log(f"Connection from: {str(address)}")
			thread_pool_exc = executor.submit(handle_client, client_sock)
			thread_pool_exc.add_done_callback(thread_pool_callback)


if __name__ == "__main__":
	server_program()

	# from bussiness import account
	# oAccountMgr = account.CAccountMgr.Inst()
	# oAccountData = oAccountMgr.CreateAccountDataByID(1024, "1314", "小可爱")
	# oAccountData.SetHeadImgUrl("038017078ce03608f27844ab098aaf20ad4a11b8ec09de3c47358083349038b9")
	# oAccountData2 = oAccountMgr.CreateAccountDataByID(2311, "520", "大可爱")
	# oAccountData.SetHeadImgUrl("08a71ed1162022dfe336b8c3800bb445cc8dc541a6da3936ecc58970d75776b2")
	# oAccountMgr.SaveAccountData(oAccountData)
	# oAccountMgr.SaveAccountData(oAccountData2)
	
