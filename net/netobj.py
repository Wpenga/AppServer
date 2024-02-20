# encoding: utf-8
'''
@author: binky
@file: netobj.py
@time: 2024/1/14 22:23
@desc:
'''


from base import single
import json


class CNetObj(single.CSingle):
	
	def __init__(self, client_socket):
		import weakref
		self.m_ClientSocketRef = weakref.ref(client_socket)
		self.m_SendData = {}
	
	def GetClientSocket(self):
		return self.m_ClientSocketRef()
	
	def Unpack(self, client_socket, dData):
		pass
	
	def Pack(self, *args):
		pass
	
	def Send(self):
		sSentData = json.dumps(self.m_SendData)
		client_socket = self.GetClientSocket()
		if client_socket:
			client_socket.send(sSentData.encode('utf-8'))
			client_socket.close()
		print("发送======")
		print(sSentData)