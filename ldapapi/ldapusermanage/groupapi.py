#coding=utf-8
from ldapapi.common.ldapconn import ldap_search,ldap_add,ldap_del,ldap_modify 
from ldapapi.ldapusermanage.setting import *
import ldap
def group_dn(groupname):
	dn = 'cn='+groupname+','+groupdn
	return dn
#ret 1:用户已存在
#    0:添加成功
#    1000:添加失败
def group_add(groupname, modlist):
	#print dn
	if is_group_exist(groupname):
		ret = 1
		result = {'msg': 'group already exists'}
	else:
		dn = group_dn(groupname)
		result = ldap_add(dn, modlist)
		#print result
		if result is not None:
			ret = 0
		else:
			ret = 1000
	#return dict({'ret':ret},**result)	
	return dict({'ret': ret, 'ldapresult':result})
def group_search(groupname,attrlist=None):
	dn = group_dn(groupname)
	ret = ldap_search(dn, '(Objectclass=*)', attrlist)
	return ret
def is_group_exist(groupname):
	ret = group_search(groupname, ['cn'])
	if ret is not None:
		return True
	else:
		return False
#ret 1:用户不存在
#    0:删除成功
#    1000:删除失败
def group_del(groupname):
	if is_group_exist(groupname) == False:
		ret = 1
		result = {'msg': 'group doesn\'t exists'}
	else:
		dn = group_dn(groupname)
		result = ldap_del(dn)
		if result is not None:
			ret = 0
		else:
			ret = 1000
	return dict({'ret': ret, 'ldapresult': result})
#ret 1:用户不存在
#    0:修改成功
#    1000:修改失败
def group_modify(groupname,modlist):
	if is_group_exist(groupname) == False:
		ret = 1
		result = {'msg':'group doesn\'t exists'}
	else:
		dn = group_dn(groupname)
		mod = []
                for i in modlist:
                        item = group_modifylist_item(groupname,i,modlist[i])
                        mod.append(item)
                print 'group_modify:mod '
                print mod
		result = ldap_modify(dn,mod)
		if result is not None:
			ret = 0
		else:
			ret = 1000
	#return dict({'ret':ret},**result)
	return dict({'ret': ret, 'ldapresult': result})
def is_group_attr_exists(groupname,attr):
        ret = group_search(groupname,[attr])
        if ret[0][1] == {}:
                return False
        else:
                return True
def group_modifylist_item(groupname, attr, val):
        if val is None:
                if is_group_attr_exists(groupname, attr):
                        return (ldap.MOD_DELETE, attr, val)
                else:
                        return ()
        else:
		return (ldap.MOD_ADD, attr, val)
