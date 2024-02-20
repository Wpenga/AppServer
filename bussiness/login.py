# encoding: utf-8
"""
@author: binky
@file: login.py
@time: 2024/1/18 22:06
@desc:
"""

from base import single
from . import account
from tools import secret

LOGIN_RESULT_SUCCESS = 1  # 登录成功
LOGIN_RESULT_PASSWORD_WRONG = 2  # 密码错误
LOGIN_RESULT_TOKEN_WRONG = 3  # Token错误
LOGIN_RESULT_ID_NOT_EXIST = 4  # 账号不存在

# 账号
class CAccountData(object):

	def __init__(self):
		pass

	def GetName(self):
		"""
		名字
		:return:
		"""
		pass

	def GetID(self):
		"""
		标识
		:return:
		"""
		pass

	def GetHeadImgUrl(self):
		"""
		头像
		:return:
		"""
		pass


class CLoginResult(object):

	def __init__(self):
		self.m_iResultCode = 0
		self.m_oAccountData = None
		self.m_sToken = ""

	def SetResultCode(self, iResultCode):
		self.m_iResultCode = iResultCode

	def GetResultCode(self):
		"""
		获取结果代码
		:return:
		"""
		return self.m_iResultCode

	def SetToken(self, sToken):
		self.m_sToken = sToken

	def GetToken(self):
		"""
		令牌
		:return:
		"""
		return self.m_sToken
	
	def SetAccountData(self, oAccountData):
		# type:(account.CAccountData) -> None
		self.m_oAccountData = oAccountData

	def GetAccountData(self):
		# type: () -> account.CAccountData
		"""
		获取账号信息
		:return:
		"""
		return self.m_oAccountData


class CLoginMgr(single.CSingle):

	@staticmethod
	def LoginInByPassword(iID, sPassword):
		# type:(int, str) -> CLoginResult
		"""
		通过密码登录
		:param iID:
		:param sPassword:
		:return:
		"""
		# 找账号
		# 验证密码
		# 生成token
		# 发送账号数据
		oLoginResult = CLoginResult()
		oAccountData = account.CAccountMgr.Inst().GetAccountDataByID(iID)
		if oAccountData:
			sEncryPassword = oAccountData.GetEncryPassword()
			sAesKey = oAccountData.GetAesKey()
			if secret.Encrypt(sAesKey, sPassword) == sEncryPassword:
				sNewToken = secret.GenRandomString(30)
				oAccountData.SetToken(sNewToken)
				oLoginResult.SetResultCode(LOGIN_RESULT_SUCCESS)
				oLoginResult.SetToken(sNewToken)
				oLoginResult.SetAccountData(oAccountData)
			else:
				oLoginResult.SetResultCode(LOGIN_RESULT_PASSWORD_WRONG)
		else:
			oLoginResult.SetResultCode(LOGIN_RESULT_ID_NOT_EXIST)
		return oLoginResult
	
	@staticmethod
	def LoginInByToken(iID, sToken):
		# type:(int, str) -> CLoginResult
		"""
		通过令牌登录
		:param iID:
		:param sToken:
		:return:
		"""
		oLoginResult = CLoginResult()
		oAccountData = account.CAccountMgr.Inst().GetAccountDataByID(iID)
		if oAccountData:
			if sToken == oAccountData.GetToken():
				oLoginResult.SetResultCode(LOGIN_RESULT_SUCCESS)
				oLoginResult.SetToken(oAccountData.GetToken())
				oLoginResult.SetAccountData(oAccountData)
			else:
				oLoginResult.SetResultCode(LOGIN_RESULT_TOKEN_WRONG)
		else:
			oLoginResult.SetResultCode(LOGIN_RESULT_ID_NOT_EXIST)
		return oLoginResult
