#coding=utf-8
from ldapapi.common.ldapconn import ldap_search,ldap_add,ldap_del,ldap_modify 
from ldapapi.ldapusermanage.setting import *
import ldap
def user_dn(username):
	dn = 'uid='+username+','+userdn
	return dn
#ret 1:用户已存在
#    0:添加成功
#    1000:添加失败
def user_add(username,modlist):
	dn = user_dn(username)
	#print dn
	if is_user_exist(username):
		ret = 1
		result = {'msg':'user already exists'}
	else:
		result = ldap_add(dn,modlist)
		#print result
		if result is not None:
			ret = 0
		else:
			ret = 1000
	#return dict({'ret':ret},**result)	
	return dict({'ret':ret,'ldapresult':result})
def user_search(username,attrlist=None):
	dn = user_dn(username)
	ret = ldap_search(dn,'(Objectclass=*)',attrlist)
	return ret
def is_user_exist(username):
	ret = user_search(username,['uid'])
	if ret is not None:
		return True
	else:
		return False
#ret 1:用户不存在
#    0:删除成功
#    1000:删除失败
def user_del(username):
	if is_user_exist(username) == False:
		ret = 1
		result = {'msg':'user doesn\'t exists'}
	else:
		dn = user_dn(username)
		result = ldap_del(dn)
		if result is not None:
			ret = 0
		else:
			ret = 1000
	return dict({'ret':ret,'ldapresult':result})
#ret 1:用户不存在
#    0:修改成功
#    1000:修改失败
def user_modify(username,modlist):
	if is_user_exist(username) == False:
		ret = 1
		result = {'msg':'user doesn\'t exists'}
	else:
		dn = user_dn(username)
		mod = []
		for i in modlist:
			item = user_modifylist_item(username,i,modlist[i])
			mod.append(item)
		print 'user_modify:mod '
		print mod
		result = ldap_modify(dn,mod)
		if result is not None:
			ret = 0
		else:
			ret = 1000
	#return dict({'ret':ret},**result)
	return dict({'ret':ret,'ldapresult':result})
def is_user_attr_exists(username,attr):
	ret = user_search(username,[attr])
	if ret[0][1] == {}:
		return False
	else:
		return True
def user_modifylist_item(username,attr,val):
	if val is None:
		if is_user_attr_exists(username,attr):
			return (ldap.MOD_DELETE,attr,val)
		else:
			return ()
	else:
		if is_user_attr_exists(username,attr):
			return (ldap.MOD_REPLACE,attr,val)
		else:
			return (ldap.MOD_ADD,attr,val)
