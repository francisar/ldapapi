__author__ = 'franciscui'
#coding=utf-8
from groupapi import *
from userapi import *

class Group:
	__objectClass = ['posixGroup', 'top', 'sambaGroupMapping']
	__cn = ''
	__sambaGroupType = 4
	__gidNumber = -1
	__displayName = ''
	__description = ''
	__sambaSID = ''
	__sambaSIDprefix = 'S-1-5-32-'
	def __init__(self, cn, sambaSIDprefix = group_sambaSID):
		self.__cn = cn
        self.__displayName = cn
        self.__sambaSIDprefix = sambaSIDprefix
	def __del__(self):
		return 0
	def add(self):
		ret = self.__add()
		#print ret
		return ret
	def __add(self):
		file = open(groupNumberURL, 'r+')
		try:
			str_gidNumber = file.read()
			file.seek(0, 0)
			self.__gidNumber = int(str_gidNumber)+1
			file.write(str(self.__gidNumber))
		finally:
			file.close()
		self.__sambaSID = self.__sambaSIDprefix + str(self.__gidNumber)
		modlist={'cn': [self.__cn], 'objectClass': self.__objectClass, 'gidNumber': [str(self.__gidNumber)],
		'description': [self.__description], 'displayName': self.__displayName, 'sambaSID': self.__sambaSID,
		'sambaGroupType': str(self.__sambaGroupType)}
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
		ret = group_modify(self.__cn, modlist)
		return ret
	def del_group(self):
		ret = group_del(self.__cn)
		return ret