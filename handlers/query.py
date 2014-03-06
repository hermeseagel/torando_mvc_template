import tornado.web
import hashlib
import datetime
import pymongo
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
import config.dbsets as dbset
'''define Query class to connection db  '''
class query():
	def __init__(self,collection,key):
		self.serverip=dbset.serverip
		self.port=dbset.port
		self.username=dbset.usename
		self.passwd=dbset.passwd
		self.dbn=dbset.db
		self.key=key
		self.collection=collection
		self.uri='mongodb://'+self.username+':'+self.passwd+'@'+self.serverip+':'+self.port+'/'+self.dbn
		self.client=pymongo.Connection(self.uri)
		self.db=self.client[self.dbn]
		#print('I am here')
		
		
	def query_mcond(self):
		cursor=self.db[self.collection].find(self.key)
		#print(type(cursor))		
		for document in cursor:
			#print(document)
			return document
	def query_one(self):
		cursor=self.db[self.collection].find_one(self.key)
		return cursor
	def insert_one(self,scollection,data):
		self.db[scollection].insert()
		
class queryHandler(tornado.web.RequestHandler):
		def get(self):
			pass
					
		def post(self):
			emaila=self.get_argument('email')
			condition={'emaila':emaila}
			if len(condition) > 0 :
				query('users',condition).query_one()
				z=b.query()
		

#stra="{'color':'green'}"
#b=query('products',{'color':'green'}).query_one()
#z=b.query_one()
#print(b['price']) 