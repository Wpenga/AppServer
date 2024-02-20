# encoding: utf-8
"""
@author: binky
@file: netlaolao.py
@time: 2023/9/27 22:47
@desc:
"""

from bussiness import laolao
from tools import log
from . import netobj


class CRequestLaolaoData(netobj.CNetObj):
	
	def Unpack(self, client_socket, dData):
		log.Log("客户端请求数据")
		iPage = dData["iPage"]
		return {
			"iPage": iPage
		}
	
	def Pack(self, dLaoLaoDataList, iPage):
		self.m_SendData["dLaoLaoDataList"] = dLaoLaoDataList
		self.m_SendData["iPage"] = iPage


class CUploadLaolao(netobj.CNetObj):
	
	def Unpack(self, client_socket, dData):
		# sFileMd5List = dData["sFileMd5List"]  # 图片的MD5
		dImgDataList = dData["dImgDataList"]  # 图片链接
		sContent = dData["sContent"]  # 内容
		sName = dData["sName"]  # 名字
		return {
			"dImgDataList": dImgDataList,
			"sContent": sContent,
			"sName": sName
		}
	
	def Pack(self, iResult):
		self.m_SendData["iResult"] = iResult


def request_laolao_data(oNetObj, dData):
	# type: (CRequestLaolaoData, dict) -> None
	print("客户端请求数据")
	iPage = dData["iPage"]
	oLaoLaoDataMgr = laolao.CLaoLaoDataMgr.Inst()
	oLaoLaoDataList = oLaoLaoDataMgr.GetLaoLaoDataByPage(iPage)
	
	dLaoLaoDataList = []
	for oLaoLaoData in oLaoLaoDataList:
		dLaoLaoData = oLaoLaoData.ToSaveData()
		dLaoLaoDataList.append(dLaoLaoData)
	
	oNetObj.Pack(dLaoLaoDataList, iPage)
	oNetObj.Send()


def upload_laolao(oNetObj, dData):
	# type: (CUploadLaolao, dict) -> None
	print("客户端上传数据")
	dImgDataList = dData["dImgDataList"]  # 图片数据
	sContent = dData["sContent"]  # 内容
	sName = dData["sName"]  # 名字
	# iUserID = dData["iUserID"]  # 用户ID
	# sToken = dData["sToken"]  # 凭证
	oLaoLaoDataMgr = laolao.CLaoLaoDataMgr.Inst()
	oLaoLaoData = oLaoLaoDataMgr.CreateLaoLaoData(sName, sContent, dImgDataList)
	oLaoLaoDataMgr.AddLaoLaoData(oLaoLaoData)
	
	oNetObj.Pack(1)
	oNetObj.Send()


class CTestClient(object):
	
	def send(self, sStr):
		pass
	
	def close(self):
		pass


# region test

def TestUnit():
	import time
	request_laolao_data(CTestClient())