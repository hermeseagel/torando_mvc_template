import os
import re
logpath='/Users/Hermes/Python_script/torando_mvc_template/logs'
fname='ddsc_db_sess.log'

def match(source,pattern):
	matchobj=re.compile(pattern)
	result=matchobj.findall(source)
#	print(len(result))
	if len(result) > 0:
		return True
	else:
		return False



class dblogparser():
	def match(source,pattern):
		matchobj=re.compile(pattern)
		result=matchobj.findall(source)
		if len(result) > 0:
			return True
		else:
			return False
	def parser(dst,filename,customer,):
		file=os.path.open(filename,'r')
	
filepat=os.path.join(logpath,fname)

print(match(fname,'ses'))

fncontent=open(filepat,'r')
data={}
j=['Customer','Server','Instance','Datetime','session','par2','par3','par4']
for lin in fncontent:
	
	lin=lin.strip()
	if  len(lin) > 0 :
		p=lin.split('|')
		#print(len(p))
		#print(type(p))
		for i in range(len(p)):
			#print(j[i],p[i])
			data[j[i]]=p[i]
			#print(i)
		#	print(p[i])
	#	data['CUSTOMER']=p[0]
	#	data['Server']=p[1]
	#	data['Instance']=p[2]
	#	data['Datetime']=p[3]
	#	data['session']=p[4]
	#	print(data)
	

fncontent.close()