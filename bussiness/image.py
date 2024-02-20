# encoding: utf-8
"""
@author: binky
@file: image.py
@time: 2024/2/3 16:01
@desc:
"""


class CImageData(object):
	
	def __init__(self):
		self.m_sOrgUrl = ""  # 原图链接
		self.m_sThumbnailUrl = ""  # 缩略图链接
	
	def SetOrgUrl(self, sOrgUrl):
		self.m_sOrgUrl = sOrgUrl
	
	def GetOrgUrl(self):
		return self.m_sOrgUrl
	
	def SetThumbnailUrl(self, sThumbnailUrl):
		self.m_sThumbnailUrl = sThumbnailUrl
	
	def GetThumbnailUrl(self):
		return self.m_sThumbnailUrl
	
	def ToSaveData(self):
		return {
			"sOrgUrl": self.m_sOrgUrl,
			"sThumbnailUrl": self.m_sThumbnailUrl,
		}
	
	def InitWithData(self, dData):
		self.m_sOrgUrl = dData["sOrgUrl"]
		self.m_sThumbnailUrl = dData["sThumbnailUrl"]
