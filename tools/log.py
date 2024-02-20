# encoding: utf-8
'''
@author: binky
@file: log.py
@time: 2023/10/19 21:13
@desc:
'''

from . import tooltime
def Log(*args):
	sCurTime = tooltime.GetCurTimeString()
	print(sCurTime, *args)
