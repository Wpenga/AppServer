# encoding: utf-8
'''
@author: binky
@file: laolao.py
@time: 2023/9/17 15:00
@desc:
'''

from tools import tooltime
import defines
from base import single
from . import image

PAGE_NUM = 10


class CLaoLaoData(object):
	
	def __init__(self):
		self.m_sName = "我是谁"
		self.m_iTime = 0
		self.m_Content = ""
		self.m_lstImgData = []
	
	def SetTime(self, iTime):
		self.m_iTime = iTime
	
	def GetTime(self):
		return self.m_iTime
	
	def SetContent(self, sContent):
		self.m_Content = sContent
	
	def GetContent(self):
		return self.m_Content

	def SetImgDataList(self, lstImgData):
		self.m_lstImgData = lstImgData

	def GetImgDataList(self):
		return self.m_lstImgData

	def SetName(self, sName):
		self.m_sName = sName

	def GetName(self):
		return self.m_sName

	def ToSaveData(self):
		return {
			"iTime": self.m_iTime,
			"sContent": self.m_Content,
			"sName": self.m_sName,
			"lstImgData": [oImgData.ToSaveData() for oImgData in self.m_lstImgData]
		}

	def InitByDict(self, dLaoLaoData):
		self.m_Content = dLaoLaoData["sContent"]
		self.m_iTime = dLaoLaoData["iTime"]
		self.m_sName = dLaoLaoData.get("sName", "游客")
		self.m_lstImgData = []
		for dImgData in dLaoLaoData["lstImgData"]:
			oImgData = image.CImageData()
			oImgData.InitWithData(dImgData)
			self.m_lstImgData.append(oImgData)


class CLaoLaoDataMgr(single.CSingle):
	
	def __init__(self):
		self.m_LaoLaoDataList = []
		self.m_oTempDataBase = CTempDataBase()
	
	def AddLaoLaoData(self, oLaoLaoData):
		# type: (CLaoLaoData) -> None
		iTime = oLaoLaoData.GetTime()
		self.m_oTempDataBase.SetLaoLaoData(iTime, oLaoLaoData)
		self.m_oTempDataBase.AddKey(iTime)
		self.m_oTempDataBase.SaveData()
	
	def CreateLaoLaoData(self, sName, sContent, dImgDataList):
		oLaoLaoData = CLaoLaoData()
		oLaoLaoData.SetContent(sContent)
		oLaoLaoData.SetName(sName)
		oLaoLaoData.SetImgDataList(dImgDataList)
		oLaoLaoData.SetTime(tooltime.GetCurTime())
		return oLaoLaoData
	
	def GetAllLaoLaoData(self):
		sKeyList = self.m_oTempDataBase.GetAllKey()
		oLaoLaoDataList = []
		for sKey in sKeyList:
			oLaoLaoDataList.append(self.m_oTempDataBase.GetLaoLaoDataByKey(sKey))
		return oLaoLaoDataList
	
	def GetLaoLaoDataByPage(self, iPage):
		sKeyList = self.m_oTempDataBase.GetAllKey()[:]
		sKeyList.reverse()
		oLaoLaoDataList = []
		for sKey in sKeyList[iPage * PAGE_NUM: (iPage + 1) * PAGE_NUM]:
			oLaoLaoDataList.append(self.m_oTempDataBase.GetLaoLaoDataByKey(sKey))
		return oLaoLaoDataList

	def SaveDataInDB(self):
		self.m_oTempDataBase.SaveData()

	def LoadFromDB(self):
		pass
	
	def SaveData(self):
		pass


class CTempDataBase(object):
	
	def __init__(self):
		self.m_KeyList = []
		self.m_LaoLaoDataDict = {}
		# self.m_PhotoDict = {}  # md5
		self.LoadFromDataBase()

	def GetLaoLaoDataByKey(self, iKey):
		return self.m_LaoLaoDataDict.get(iKey)
	
	def GetAllKey(self):
		return self.m_KeyList
	
	def AddKey(self, iKey):
		if iKey not in self.m_KeyList:
			self.m_KeyList.append(iKey)
	
	def SetKeyList(self, iKeyList):
		self.m_KeyList = iKeyList

	def SetLaoLaoData(self, iKey, dData):
		self.m_LaoLaoDataDict[iKey] = dData

	def SaveData(self):
		from tools import datatools
		import json
		sDataBase = defines.DATA_BASE
		sTableName = defines.TABLE_LAOLAO_PUSH
		datatools.create_table(sDataBase, sTableName)
		dLaoLaoData = {}
		for iTime, oLaoLaoData in self.m_LaoLaoDataDict.items():
			dLaoLaoData[iTime] = oLaoLaoData.ToSaveData()
		sLaoLaoData = json.dumps(dLaoLaoData)
		sKeyList = json.dumps(self.m_KeyList)
		datatools.update_data(sDataBase, sTableName, "laolao_data", sLaoLaoData)
		datatools.update_data(sDataBase, sTableName, "sKeyList", sKeyList)

	def LoadFromDataBase(self):
		from tools import datatools
		import json
		sDataBase = defines.DATA_BASE
		sTableName = defines.TABLE_LAOLAO_PUSH
		datatools.create_table(sDataBase, sTableName)
		
		tLaoLaoData = datatools.find_data(sDataBase, sTableName, "laolao_data")
		sLaoLaoData = tLaoLaoData[1] if tLaoLaoData else None

		tPhotoData = datatools.find_data(sDataBase, sTableName, "photo")
		sPhotoData = tPhotoData[1] if tPhotoData else None

		tKeyList = datatools.find_data(sDataBase, sTableName, "sKeyList")
		sKeyList = tKeyList[1] if tKeyList else None

		print(sLaoLaoData)
		print(sPhotoData)
		print(sKeyList)
		if sLaoLaoData:
			dLaoLaoData = json.loads(sLaoLaoData)
			for sKey, dLaoLao in dLaoLaoData.items():
				oLaoLaoData = CLaoLaoData()
				oLaoLaoData.InitByDict(dLaoLao)
				self.m_LaoLaoDataDict[sKey] = oLaoLaoData
		if sKeyList:
			iKeyList = json.loads(sKeyList)
			for iKey in iKeyList:
				self.m_KeyList.append(str(iKey))


"""
数据结构：
1. 记录索引，时间作为key值
2. 记录数据
3.

"""

# page管理器
# 数据进来
# 数据分页，新的在最前面。每页数据固定5条
class CPageMgr(object):

	def __init__(self):
		pass

	def AddDataKey(self, sDataKey):
		pass

	def GetDataKeyList(self, iPage):
		pass
