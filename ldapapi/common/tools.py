#coding=utf-8
class switch(object):
	def __init__(self,value):
		self.__value = value
		self.__fall = False
	def __iter__(self):
		yield self.__match
		raise StopIteration
	def __match(self,*args):
		if self.__fall or not args:
			return True
		elif self.__value in args:
			self.__value = True
			return True
		else:
			return False
