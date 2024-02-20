# encoding: utf-8
'''
@author: binky
@file: netversion.py
@time: 2024/1/14 20:26
@desc:
'''
import version
from . import netobj


# 请求版本信息
class CRequestVersionInfo(netobj.CNetObj):

	def Unpack(self, client_socket, dData):
		return {}

	def Pack(self, iVersionRelease):
		self.m_SendData["iVersionRelease"] = iVersionRelease


# 请求最新的APK
class CRequestNewestApk(netobj.CNetObj):
	
	def Unpack(self, client_socket, dData):
		return {}
	
	def Pack(self):
		sApkData = open(version.NEWEST_APK_PATH, "rb").read()
		self.m_SendData["sApkFileData"] = sApkData


# 请求版本信息
def request_version_info(oNetObj, dData):
	# type: (CRequestVersionInfo, dict) -> None
	oNetObj.Pack(version.VERSION_RELEASE)
	oNetObj.Send()


# 请求最新的APK
def request_newest_apk(oNetObj, dData):
	# type: (CRequestNewestApk, dict) -> None
	oNetObj.Pack()
	oNetObj.Send()
