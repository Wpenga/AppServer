# encoding: utf-8
"""
@author: binky
@file: mgrnet.py
@time: 2024/1/14 22:00
@desc:
"""

from base import single
from . import defines
from tools import log


def HandOut(client_socket, dData):
	# 分发
	sSub = dData["sub_string"]
	CNetObj, oCallBack = defines.REQUEST_2_NET_OBJECT.get(sSub, (None, None))
	if CNetObj:
		log.Log("收到请求", sSub)
		oNetObj = CNetObj(client_socket)
		dUnpackData = oNetObj.Unpack(client_socket, dData)
		oCallBack(oNetObj, dUnpackData)
	else:
		log.Log("请求的意义不明===", sSub)
		client_socket.send("ACK!".encode('utf-8'))


class CMgr(single.CSingle):

	def __init__(self):
		pass
