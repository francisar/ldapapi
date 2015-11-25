#coding=utf-8
from groupapi import *
from userapi import *

class People:
	__objectClass = ['posixAccount', 'top', 'shadowAccount', 'person', 'organizationalPerson', 'inetOrgPerson', 'sambaSamAccount']
	__cn = ''
	__gidNumber = -1
	__homeDirectory = ''
	__loginShell = '/sbin/nologin'
	__passwd = ''
	__userid = ''
	__uidNumber = -1
	__host = []
	__gecos = ''
	__sambaAcctFlags = '[U          ]'
	__sambaHomeDrive = 'H:'
	__sambaHomePath = ''
	__sambaKickoffTime = 2147483647
	__sambaLogoffTime = 2147483647
	__sambaLMPassword = ''
	__sambaLogonTime = 0
	__sambaNTPassword = ''
	__sambaPrimaryGroupSID = ''
	__sambaProfilePath = ''
	__sambaPwdCanChange = 0
	__sambaPwdLastSet = 1439970241
	__sambaPwdMustChange = 2147483647
	__sambaSID = ''
	__shadowLastChange = 16666
	__sn = ''
	__sambaSIDprefix = ''
	def __init__(self,userid, sambaSIDprefix = domain_sambaSID):
		self.__sn = userid
		self.__sambaSIDprefix = sambaSIDprefix + '-'
		self.__userid = userid
		self.__homeDirectory = '/data/home/' + self.__userid
		self.__sambaProfilePath = '\\\\PDC-SRV\\profiles\\' + self.__userid
		self.__sambaHomePath = '\\\\PDC-SRV\\' + self.__userid
	def __del__(self):
		return 0
	def add(self, cn, gidNumber = 1000):
		self.__cn = cn
		self.__gidNumber = gidNumber
		ret = self.__add()
		#print ret
		return ret
	def __add(self):
		file = open(userNumberURL, 'r+')
		try:
			str_userNumber = file.read()
			file.seek(0,0)
			self.__uidNumber = int(str_userNumber)+1
			file.write(str(self.__uidNumber))
		finally:
			file.close()
		self.__sambaPrimaryGroupSID = self.__sambaSIDprefix + str(self.__gidNumber)
		self.__sambaSID = self.__sambaSIDprefix + str(self.__uidNumber)
		modlist={'cn': [self.__cn], 'objectClass': self.__objectClass, 'gidNumber': [str(self.__gidNumber)],
		'homeDirectory': [self.__homeDirectory], 'loginShell': [self.__loginShell], 'userid':[self.__userid],
		'uidNumber': [str(self.__uidNumber)], 'sn': [self.__sn], 'gecos': [self.__gecos],
		'sambaAcctFlags': self.__sambaAcctFlags, 'sambaHomeDrive': self.__sambaHomeDrive,
		'sambaHomePath': [self.__sambaHomePath], 'sambaKickoffTime': str(self.__sambaKickoffTime),
		'sambaLogoffTime': str(self.__sambaLogoffTime), 'sambaLogonTime': str(self.__sambaLogonTime),
		'sambaPrimaryGroupSID': self.__sambaPrimaryGroupSID, 'sambaProfilePath': self.__sambaProfilePath,
		'sambaPwdCanChange': str(self.__sambaPwdCanChange), 'sambaPwdLastSet': str(self.__sambaPwdLastSet),
		'sambaPwdMustChange': str(self.__sambaPwdMustChange), 'sambaSID': self.__sambaSID,
		'shadowLastChange': str(self.__shadowLastChange)}
		ret = user_add(self.__userid, modlist)
		#print ret
		return ret
#	def __is_attr_exists(attr):
#		ret = user_search(__userid,[attr]):
#		if ret[0][1] == {}:
#			return False
#		else:
#			return True 
#	def __set_attr_list(attr,val):
#		if val is None:
#			if __is_attr_exists(attr)
#				return ()
	def __modify(self, modlist):
		if modlist.has_key('uidNumber'):
			del modlist['uidNumber']
		ret = user_modify(self.__userid, modlist)
		return ret
	def del_people(self):
		ret = user_del(self.__userid)
		return ret
	def host_authorize(self, host):
		if is_user_exist(self.__userid) == False:
			ret = self.add()
			if ret['ret'] != 0:
				return ret
		modlist = {}
		ldapuser = 500
		modlist['host'] = host
		modlist['loginShell'] = '/bin/bash'
		modlist['gidNumber'] = str(ldapuser)
		ret = self.__modify(modlist)
		return ret
	def set_passwd(self, passwd):
		if is_user_exist(self.__userid) == False:
			return {'ret': 1, 'msg': 'user doesn\'t exists'}
		modlist = {'userPassword': passwd, 'sambaLMPassword': passwd, 'sambaNTPassword': passwd}
		ret = self.__modify(modlist)
		return ret
	def openvpn_authorize(self, groupname):
		if is_group_exist(groupname):
			modlist = {'member': user_dn(self.__userid)}
			ret = group_modify(groupname, modlist)
			return ret
		else:
			return {'ret': 1, 'msg': 'group doesn\'t exists'}
		
