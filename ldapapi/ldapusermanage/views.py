#coding=utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
import simplejson
from ldapapi.common.tools import switch
from setting import openvpn_group1
from People import *
# Create your views here.
@csrf_exempt
def user(request):
	try:
		if request.method == 'POST':
			#req = simplejson.loads(request.raw_post_data)
			result = None
			#droplistname = req['droplistname']
			action=str(request.POST.get('action', ''))
			for case in switch(action):
				if case('adduser'):
					username=str(request.POST.get('username', ''))
					cn=request.POST.get('cn', '').encode('utf8')
					#print  self.__MsgType+self.__ToUserName+self.__FromUserName+self.__CreateTime+self.__Content
					p = People(username.strip())
					result = p.add(cn)
					#result 
					break
				if case('deluser'):
					username=str(request.POST.get('username', ''))
					#print  self.__MsgType+self.__ToUserName+self.__FromUserName+self.__CreateTime+self.__Content
					p = People(username.strip())
					result = p.del_people()
					#result 
					break
				if case('setpasswd'):
					#print self.__MsgType
					#return self.__image()
					username=str(request.POST.get('username', ''))
					passwd=str(request.POST.get('passwd', ''))
					p = People(username.strip())
					result = p.set_passwd(passwd.strip())
					#username = self.__args.split(' ',1)[0]
					#api = LdapApi(username,self.__iplist)
					#self.__result = api.call({'action': 'adduser'})
					break
				if case('vpnon'):
					username = str(request.POST.get('username', ''))
					p = People(username.strip())
					result = p.openvpn_authorize(openvpn_group1)
					break
				if case():
					#result = p.set_passwd(passwd.strip())
					break
				#if case('voice'):
					#print self.__MsgType
				#	return self.__voice()
				#	break	
				#print 'user response:'+username+','+passwd+','+action
			return HttpResponse(simplejson.dumps(result,ensure_ascii = False))
		else:
			result = {'ret':2,'msg':'method must be post'}
			return HttpResponse(simplejson.dumps(result,ensure_ascii = False))
	except:
		import sys
		info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
		print info
