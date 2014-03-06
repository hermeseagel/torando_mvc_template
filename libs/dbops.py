import pymongo,os,sys  
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import config.dbsets as dbset 
class dbobsbase(object):
	def __init__(self):
		self.serverip=dbset.serverip
		self.port=dbset.port
		self.username=dbset.usename
		self.passwd=dbset.passwd
		self.dbn=dbset.db
		self.uri='mongodb://'+self.username+':'+self.passwd+'@'+self.serverip+':'+self.port+'/'+self.dbn
		self.client=pymongo.Connection(self.uri)
		self.db=self.client[self.dbn]
		
class dbwrite(dbobsbase):
	def __init__(self,scollection,data):
		super(dbwrite,self).__init__()
		self.data=data
		self.collect=scollection
	def insert(self):
		#self.client.authenticate(self.username,self.passwd)
		print('write to data')
		self.db[self.collect].insert(self.data)
	

class dbquery(dbobsbase):		
	def __init__(self,scollection,key):
		super(dbquery,self).__init__()
		self.collect=scollection
		self.key=key
	def query_one(self):	
		cursor=self.db[self.collect].find_one(self.key)
		return cursor		 
		
	def delete_one(self):
		cursor=self.db[self.collect].remove(self.key)
		return cursor
		
#a=dbquery('sysconfig',{'index':'logtype'}).query_one()
#b=dbwrite('sysconfig',{'hermes':'test'}).insert()