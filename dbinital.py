import re
from pymongo import MongoClient
import config.dbsets as dbset
'''initial mongodb data set '''
logtype={'index':'logtype','session':'sess','tablespace':'tbs','segament':'seg','UNDO':'undo','PGA':'pga'}
sess={'logtype':'sess','para0':'cust_id','para1':'instance','para2':'sampletime','para3':'active','para4':'inactive','para5':'total'}
tbs={'logtype':'tbs','para0':'cust_id','para1':'host','para2':'inst_name','para3':'sample_time',
'para4':'tablespace','para5':'total','para6':'megs_alloc','para7':'megs_used'}
arch={'logtype':'arch'}


def initalstep():
	'''Read Setting from directory Config/dbsets.py  '''
	serverip=dbset.serverip
	port=dbset.port
	uri=dbset.url
	db=dbset.db
	username=dbset.usename
	password=dbset.passwd
	'''start connection to mongodb 
	for mongodb authenticate mode must use uri 
	url="mongodb://usename:passwd@serverip:port/dbname "
	 '''
	client=MongoClient(uri)
	'''after connection  to connection  
	acutally it is pymongo limit  (uri) define db but not really enter to db must work agin
	
	'''
	db=client[db]
	''' enter db must key your id and password to get permission 
	take care mongodb admin role quite different 
	
 	roles as below:  (normal user must be readWrite then you can insert, update , delete)
   * read
   * readWrite
   * dbAdmin
   * userAdmin
   * clusterAdmin
   * readAnyDatabase
   * readWriteAnyDatabase
   * userAdminAnyDatabase
	if you set as dbAdminAnyDatabase you just can managment collections and build index 
	you can not insert data 
   * dbAdminAnyDatabase

	
	'''
	
	
	'''-
	enter to sysconfig collection
	-'''
	
	db.authenticate(username,password)
	collect=db['sysconfig']
	print(logtype.values())
	for para in logtype.values():
		#print(para)
		#print(collect.find({"logtype":para}).count())
		if collect.find({"logtype":para}).count() >0 or collect.find({"index":"logtype"}).count() > 0 :
			pass
		elif collect.find({"index":"logtype"}).count() ==0 :
			collect.insert(logtype)
			collect.insert(sess)
			collect.insert(tbs)


	
	
initalstep()