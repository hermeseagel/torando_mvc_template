import os,sys
import re
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from handlers.query import query
#logpath='/Users/Hermes/Python_script/torando_mvc_template/logs'
fname='ddsc_db_sess.log'

#def match(source,pattern):
#	matchobj=re.compile(pattern)
#	result=matchobj.findall(source)
#	print(len(result))
#	if len(result) > 0:
#		return True
#	else:
#		return False



class dblogparser:
	def match(source,pattern):
		matchobj=re.compile(pattern)
		result=matchobj.findall(source)
		if len(result) > 0:
			return True
		else:
			return False

	def parser(dst,filename,datestamp):
		filelocation = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		dst=os.path.join(filelocation,dst)
		fn=os.path.join(dst,filename)
		print(fn)
		logtype={'index':'logtype'}
		result=query('sysconfig',logtype).query_one()
		#print(result)
		'''below actions just for get logs mapping from db record  '''
		pa={}
		for key,value in result.items() :
			#print(type(value),value)
			if key != '_id'  and key !='index' :
				if dblogparser.match(filename,value)==True:
					print(value)
					paras=query('sysconfig',{'logtype':value}).query_one()
					for pkey,para in paras.items():
						if pkey !='_id' and pkey !='logtype':
							pa[pkey]=para
			else:
			#	print(value)
				pass
		print(pa)
		file=open(fn,'r')
		for line in file:
			stripline=line.strip()
			if len(stripline) >0:
				fileds=stripline.split('|')
				jall={}
				for filednum in range(len(fileds)):
					lookey='para'+str(filednum)
					jkey=pa.get(lookey)
					jvalue=fileds[filednum]
					#print(jkey,':',jvalue)
					jall[jkey]=jvalue
				jall['datestamp']=datestamp
				#print(jall)
		file.close()



#dblogparser.parser(logpath,fname,'20140202')

#filepat=os.path.join(logpath,fname)

#print(match(fname,'ses'))

#fncontent=open(filepat,'r')
#data={}
#j=['Customer','Server','Instance','Datetime','session','par2','par3','par4']
#for lin in fncontent:
	
#	lin=lin.strip()
#	if  len(lin) > 0 :
#		p=lin.split('|')
		#print(len(p))
		#print(type(p))
#		for i in range(len(p)):
			#print(j[i],p[i])
#			data[j[i]]=p[i]
			#print(i)
		#	print(p[i])
	#	data['CUSTOMER']=p[0]
	#	data['Server']=p[1]
	#	data['Instance']=p[2]
	#	data['Datetime']=p[3]
	#	data['session']=p[4]
	#	print(data)
	

#fncontent.close()