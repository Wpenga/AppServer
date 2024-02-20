# encoding: utf-8
"""
@author: binky
@file: defines.py
@time: 2024/1/14 20:34
@desc:
"""

DEBUG = 0
if DEBUG:
	# HOST = "192.168.31.35"
	HOST = "192.168.31.111"
else:
	HOST = "10.0.12.15"
PORT = 55586

DATA_BASE = "laolao.db"
TABLE_LAOLAO_PUSH = "laolao_push"

DATA_ACCOUNT = "account.db"
TABLE_ACCOUNT = "account"