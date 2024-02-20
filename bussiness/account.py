# encoding: utf-8
"""
@author: binky
@file: account.py
@time: 2024/1/18 22:53
@desc:
"""
import json
import defines
from base import single
from tools import datatools
from tools import secret


# 账号
class CAccountData(object):

	def __init__(self):
		self.m_sImgUrl = ""
		self.m_sName = ""
		self.m_sToken = ""
		self.m_iID = 0
		self.m_sAesKey = ""  # 秘钥
		self.m_sEncryPassword = ""  # 加密的密码

	def SetName(self, sName):
		self.m_sName = sName

	def GetName(self):
		"""
		名字
		:return:
		"""
		return self.m_sName

	def SetID(self, iID):
		self.m_iID = iID

	def GetID(self):
		"""
		标识
		:return:
		"""
		return self.m_iID

	def SetHeadImgUrl(self, sImgUrl):
		self.m_sImgUrl = sImgUrl

	def GetHeadImgUrl(self):
		"""
		头像
		:return:
		"""
		return self.m_sImgUrl

	def SetToken(self, sToken):
		self.m_sToken = sToken

	def GetToken(self):
		return self.m_sToken

	def SetAesKey(self, sAesKey):
		self.m_sAesKey = sAesKey

	def GetAesKey(self):
		return self.m_sAesKey

	def SetEncryPassword(self, sEncryPassword):
		self.m_sEncryPassword = sEncryPassword

	def GetEncryPassword(self):
		return self.m_sEncryPassword

	def ToSaveData(self):
		return {
			"iID": self.m_iID,
			"sName": self.m_sName,
			"sImgUrl": self.m_sImgUrl,
			"sToken": self.m_sToken,
			"sEncryPassword": self.m_sEncryPassword,
			"sAesKey": self.m_sAesKey,
		}

	def InitFromData(self, dData):
		self.m_iID = dData["iID"]
		self.m_sName = dData["sName"]
		self.m_sImgUrl = dData["sImgUrl"]
		self.m_sToken = dData["sToken"]
		self.m_sEncryPassword = dData["sEncryPassword"]
		self.m_sAesKey = dData["sAesKey"]


# 账号管理
class CAccountMgr(single.CSingle):

	def __init__(self):
		datatools.create_database(defines.DATA_ACCOUNT)
		datatools.create_table(defines.DATA_ACCOUNT, defines.TABLE_ACCOUNT)

	def GetAccountDataByID(self, iID):
		# type:(int) -> CAccountData | None
		"""
		通过ID拿到账号数据
		:param iID:
		:return:
		"""
		sData = datatools.find_data(defines.DATA_ACCOUNT, defines.TABLE_ACCOUNT, iID)
		sAccountData = sData[1] if sData else None
		if sAccountData:
			dData = json.loads(sAccountData)
			oAccountData = CAccountData()
			oAccountData.InitFromData(dData)
			return oAccountData
		else:
			return None

	def SaveAccountData(self, oAccountData):
		# type:(CAccountData) -> None
		"""
		存账号数据
		:param oAccountData:
		:return:
		"""
		iID = oAccountData.GetID()
		sLaoLaoData = json.dumps(oAccountData.ToSaveData())
		datatools.update_data(defines.DATA_ACCOUNT, defines.TABLE_ACCOUNT, iID, sLaoLaoData)

	def CreateAccountDataByID(self, iID, sPassword, sName):
		# type:(int, str, str) -> CAccountData
		"""
		创建一个账号
		:param iID:
		:param sPassword:
		:param sName:
		:return:
		"""
		oAccountData = CAccountData()
		oAccountData.SetID(iID)
		oAccountData.SetName(sName)
		# 创建token
		# 创建aes-key
		sAesKey = secret.GenRandomString(16)
		sToken = secret.GenRandomString(20)
		oAccountData.SetAesKey(sAesKey)
		oAccountData.SetToken(sToken)
		sEncryPassword = secret.Encrypt(sAesKey, sPassword)
		oAccountData.SetEncryPassword(sEncryPassword)
		return oAccountData
