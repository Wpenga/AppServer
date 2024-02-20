# encoding: utf-8
'''
@author: binky
@file: tooltime.py
@time: 2023/9/17 14:56
@desc:
'''

from datetime import datetime
import time


def GetCurTime():
	currentDateAndTime = datetime.now()
	return int(currentDateAndTime.timestamp())


def GetCurTimeString():
	timestamp = GetCurTime()
	formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))
	return formatted_time
