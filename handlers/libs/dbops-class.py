import pymongo  
class dbconn():
	def __init__(self,serverip,port):
		#self.serverip='10.37.129.4'
		#self.port=27017
		#self.port=port
		self.serverip=serverip
		self.dbsvr=pymongo.Connection(self.serverip,self.port)
		#print(self.condition)
	def connect(self):
		self.dbsvr=pymongo.Connection(self.serverip,self.port)
		
class dbquery(dbconn):		
	def __init__(self,serverip,port,db,collection,condition,key):
		dbconn()
		self.port=port
		self.
	def query():	
		print(db,collection,condition,key)
		collect=self.dbsvr[db]
		docume=collect[collection]
		print(key)
		queryitem={key:''}
		if len(conditon) == 0 :
			print('condition no exist')
		else:
			for list in db[db].find(conditon,queryitem):
				result=list.get(key,0)
				print(result)
				return result
	def lists(self):
		print(self.condition)
	
#dbsets={'serverip':'10.37.129.4','port':'27017','user':'name'}

username='bcd001'		
condition={'user_id':username}
key='age'
p=dbops()
p.lists()

#print(dbops.query('hermes','haha',condition,key))