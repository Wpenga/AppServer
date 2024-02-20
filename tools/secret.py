# encoding: utf-8
"""
@author: binky
@file: secret.py
@time: 2024/1/20 19:56
@desc:
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import string
import base64

IV = "1234568890123458"


def Encrypt(sAesKey, sText):
	return CAesEncrypt(sAesKey).encrypt(sText)


def Decrypt(sAesKey, sEncryptText):
	return CAesEncrypt(sAesKey).decrypt(sEncryptText)


class CAesEncrypt(object):
	
	def __init__(self, sAesKey):
		self.key = sAesKey
		self.mode = AES.MODE_CBC
		iAesKeyLen = len(sAesKey)
		self.m_PadFunc = lambda s: s + (iAesKeyLen - len(s) % iAesKeyLen) * chr(iAesKeyLen - len(s) % iAesKeyLen)
		self.m_UnpadFunc = lambda s: s[0:-ord(s[-1:])]
		self.ciphertext = None
	
	# 加密函数
	def encrypt(self, text):
		cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
		self.ciphertext = cryptor.encrypt(bytes(self.m_PadFunc(text), encoding="utf8"))
		# AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
		return base64.b64encode(self.ciphertext).decode()
	
	# 解密函数
	def decrypt(self, text):
		text = bytes(text, encoding="utf8")
		decode = base64.b64decode(text)
		cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
		plain_text = cryptor.decrypt(decode)
		return self.m_UnpadFunc(plain_text).decode()


def GenRandomString(length):
	"""
	简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
	"""
	chars = string.ascii_letters + string.digits
	# return ''.join([random.choice(chars) for i in range(length)])  # 得出的结果中字符会有重复的
	return ''.join(random.sample(chars, length))  # 得出的结果中字符不会有重复的
