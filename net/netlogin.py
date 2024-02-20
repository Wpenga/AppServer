# encoding: utf-8
"""
@author: binky
@file: netlogin.py
@time: 2024/1/20 20:51
@desc:
"""


from . import netobj
from bussiness import login


# 通过密码登录
class CLoginInByPassword(netobj.CNetObj):
	
	def Unpack(self, client_socket, dData):
		return {
			"iID": dData["iID"],
			"sPassword": dData["sPassword"],
		}
	
	def Pack(self, iResult, sToken, sName, sHeadImgUrl):
		"""
		:param iResult: 登录结果
		:param sToken: 登录凭证，用于之后的自动登录
		:param sName: 用户昵称
		:param sHeadImgUrl: 头像URL
		:return:
		"""
		self.m_SendData["iResult"] = iResult
		self.m_SendData["sToken"] = sToken
		self.m_SendData["sName"] = sName
		self.m_SendData["sHeadImgUrl"] = sHeadImgUrl


# 通过令牌登录
class CLoginInByToken(netobj.CNetObj):
	
	def Unpack(self, client_socket, dData):
		return {
			"iID": dData["iID"],
			"sPassword": dData["sPassword"],
		}
	
	def Pack(self, iResult, sToken, sName, sHeadImgUrl):
		"""
		:param iResult: 登录结果
		:param sToken: 登录凭证，用于之后的自动登录
		:param sName: 用户昵称
		:param sHeadImgUrl: 头像URL
		:return:
		"""
		self.m_SendData["iResult"] = iResult
		self.m_SendData["sToken"] = sToken
		self.m_SendData["sName"] = sName
		self.m_SendData["sHeadImgUrl"] = sHeadImgUrl


# 通过密码登录
def login_in_by_password(oNetObj, dData):
	# type: (CLoginInByPassword, dict) -> None
	# 登录
	oLoginResult = login.CLoginMgr.Inst().LoginInByPassword(dData["iID"], dData["sPassword"])
	iResult = oLoginResult.GetResultCode()
	if iResult == login.LOGIN_RESULT_SUCCESS:
		sToken = oLoginResult.GetToken()
		oAccountData = oLoginResult.GetAccountData()
		sName = oAccountData.GetName()
		sHeadImgUrl = oAccountData.GetHeadImgUrl()
	else:
		sToken = ""
		sName = ""
		sHeadImgUrl = ""
	oNetObj.Pack(iResult, sToken, sName, sHeadImgUrl)
	oNetObj.Send()


def login_in_by_token(oNetObj, dData):
	oLoginResult = login.CLoginMgr.Inst().LoginInByToken(dData["iID"], dData["sPassword"])
	iResult = oLoginResult.GetResultCode()
	if iResult == login.LOGIN_RESULT_SUCCESS:
		sToken = oLoginResult.GetToken()
		oAccountData = oLoginResult.GetAccountData()
		sName = oAccountData.GetName()
		sHeadImgUrl = oAccountData.GetHeadImgUrl()
	else:
		sToken = ""
		sName = ""
		sHeadImgUrl = ""
	oNetObj.Pack(iResult, sToken, sName, sHeadImgUrl)
	oNetObj.Send()
