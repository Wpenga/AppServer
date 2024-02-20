# encoding: utf-8
"""
@author: binky
@file: defines.py
@time: 2024/1/14 21:00
@desc:
"""
from . import netversion
from . import netlaolao
from . import netlogin

REQUEST_2_NET_OBJECT = {
	"request_version_info": (netversion.CRequestVersionInfo, netversion.request_version_info),
	"request_newest_apk": (netversion.CRequestNewestApk, netversion.request_newest_apk),
	"request_laolao_data": (netlaolao.CRequestLaolaoData, netlaolao.request_laolao_data),
	"upload_laolao": (netlaolao.CUploadLaolao, netlaolao.upload_laolao),
	"login_in_password": (netlogin.CLoginInByPassword, netlogin.login_in_by_password),
	"login_in_token": (netlogin.CLoginInByToken, netlogin.login_in_by_token),
}
