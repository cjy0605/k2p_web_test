# -*- coding: UTF-8 -*-
#!/usr/bin/env python
############################################################
#
# FILE NAME  :   
# VERSION    :   1.0
# DESCRIPTION:   修改管理员密码
# AUTHOR     :   LiuLu <lu.liu@phicomm.com>
# CREATE DATE:   04/06/2017
#
##############################################################
import adapter, log, configApi
import time, sys
sys.path.append('../data')
import loginData

class changePwdClass(object):
	"""docstring for changePwdClass"""
	def __init__(self, arg):
		self.pwdNew = arg['pwdNew']
		if arg['pwdOld'] != "*":
			self.pwdOld = arg['pwdOld']
		else:
			self.pwdOld = loginData.login_data['login_pwd']

	def changeUserPwd(self):
		adapter.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]')
		adapter.waitandClick('//*[@id="Con"]/div[1]/ul[2]/li[1]/ul/li[3]')
		adapter.waitforDisplay('//*[@id="_Widget"]')
		adapter.waitandSendkeys('//*[@id="PwdOld"]', self.pwdOld)
		adapter.waitandSendkeys('//*[@id="PwdNew"]', self.pwdNew)
		adapter.waitandSendkeys('//*[@id="PwdCfm"]', self.pwdNew)

		adapter.waitandClick('//*[@id="SavePwd"]')
		time.sleep(1)
		if adapter.elementIsDisplayed('//*[@id="Pwd"]'):
			configApi.cfgSet('loginData', 'login_data', 'login_pwd', self.pwdNew)

def main(data):
	log.writeLog(data, 'changeUserPwd', 1)
	changePwdObj = changePwdClass(data)
	changePwdObj.changeUserPwd()
	log.writeLog(data, 'changeUserPwd', 2)