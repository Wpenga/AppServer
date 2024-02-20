# encoding: utf-8
'''
@author: binky
@file: filetools.py
@time: 2023/9/27 22:37
@desc:
'''

import hashlib


def GetStrMd5(sStr):
	md5 = hashlib.md5(sStr.encode("utf-8")).hexdigest()
	return md5
