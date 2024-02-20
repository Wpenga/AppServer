# encoding: utf-8
"""
@author: binky
@file: single.py
@time: 2024/1/14 21:13
@desc:
"""


# 单例
class CSingle(object):
	s_Inst = None

	@classmethod
	def Inst(cls):
		if not cls.s_Inst:
			cls.s_Inst = cls()
		return cls.s_Inst
