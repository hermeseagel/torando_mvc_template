import pymongo
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import config.dbsets as dbsets
def query(serverip,port,db,collection,condition,key):
	dbsvr=pymongo.Connection(serverip,port)
	#print(type(dbsvr))
	#print(db,collection,condition,key)
	collect=dbsvr[db]
	docume=collect[collection]
	#print(key)
	queryitem={key:''}
	if len(condition) == 0 :
			print('condition no exist')
	else:
		for list in collect[collection].find(condition,queryitem):
			result=list.get(key,0)
			#print(result)
			return result
def insert(serverip,port,db,collection,data):
	dbsvr=pymongo.Connection(serverip,port)
	collect=dbsvr[db]
	docume=collect[collection]
	if len(data) > 0 :
		docume.insert(data)
	else:
		pass

	
#serverip='10.37.129.4'
#port=27017
#username='bcd001'
#db='hermes'
#collection='haha'		
#condition={'user_id':username}
#key='age'
#print(query(serverip,port,db,collection,condition,key))