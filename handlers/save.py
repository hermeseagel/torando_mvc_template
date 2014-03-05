import tornado.web
import hashlib
import datetime
import pymongo
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
import config.dbsets as dbset




class insert():
	def __init__(self,collection,data):
		self.serverip=dbset.serverip
			self.port=dbset.port
			self.username=dbset.usename
			self.passwd=dbset.passwd
			self.dbn=dbset.db
			self.key=key
			self.collection=collection
			self.uri='mongodb://'+self.username+':'+self.passwd+'@'+self.serverip+':'+self.port+'/'+self.dbn
			self.client=pymongo.Connection(self.uri)
			self.data=data
			self.db=self.client[self.dbn]
	def save():
		cursor=self.db[self.collection].insert(self.data)
		return True
		


class updatebykey(query):
	def __init__(self,postdata):
		super(query, self).__init__(key)
		self.postdata=postdata
	def update(self):
		pass