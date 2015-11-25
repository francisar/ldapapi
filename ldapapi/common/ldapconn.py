#coding=utf-8
import ldap,ldap.modlist
from ldapapi.settings import LDAP_SERVER,LDAP_BIND,LDAP_PASS
def ldap_conn():
	try: 
		conn = ldap.initialize(LDAP_SERVER) 
		conn.protocol_version = ldap.VERSION3
		username = LDAP_BIND 
		password = LDAP_PASS
		conn.simple_bind_s(username,password) 
		#print conn
		return conn
	except ldap.LDAPError, e: 
		print e 
def ldap_add(dn,modlist):
	try:
		conn=ldap_conn()
		#print dn
		#print modlist
		mod = ldap.modlist.addModlist(modlist)
		ret = conn.add_s(dn,mod)
		return ret
	except ldap.LDAPError, e:
		print e
def ldap_del(dn):
	try:
		conn=ldap_conn()
		#print dn
		ret = conn.delete_s(dn)
		return ret
	except ldap.LDAPError, e:
		print e
def ldap_modify(dn,modlist):
	try:
		conn=ldap_conn()
		#print dn
		#print modlist
		ret = conn.modify_s(dn,modlist)
		return ret
	except ldap.LDAPError, e:
		print e
def ldap_search(base,searchFilter='(Objectclass=*)',attrlist=None,attrsonly=0):
	try:
		conn=ldap_conn()
		searchScope = ldap.SCOPE_SUBTREE
		result_set = conn.search_s(base,searchScope,searchFilter,attrlist,attrsonly)
		#result_set = []
		return result_set
	except ldap.LDAPError, e:
		print e
