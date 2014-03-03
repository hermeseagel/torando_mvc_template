import tornado.web
import tornado.ioloop
import hashlib
import tornado.gen
#import moto
import hashlib
import datetime
import motor 
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
import config.dbsets as dbset
class query():
	def __init__(self,collection,key):
		self.ip=dbset.serverip
		self.port=dbset.port
		self.username=dbset.usename
		self.passwd=dbset.passwd
		self.db=dbset.db
		self.key=key
		uri=uri='mongodb://'+self.username+':'+self.passwd+'@'+self.serverip+':'+self.port+'/'+db
		self.client=motor.MotorClient(uri).open_sync()
		
		
	def query_mcond(self):
		cursor=db[collect].find({"key":self.key })
		