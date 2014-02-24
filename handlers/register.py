import tornado.web
import tornado.ioloop
import hashlib
import tornado.gen
#import pymongo
import hashlib
import datetime


class  reghandler(tornado.web.RequestHandler):
	
	def get(self):
		#db = pymongo.Connection('10.37.129.4',27017)
		#userdb=db.conn
		print('render reg.html')
		self.render('reg.html')
	def post(self):
		companyname=self.get_argument('companyname')
		username=self.get_argument('username')
		password=self.get_argument('pass1')
		emaila=self.get_argument('emailaddr')
		encryptstr=hashlib.sha256(password.encode()).hexdigest()
		print('user.html',username)
		data={'companyname':companyname,'username':username,'password':encryptstr,}
		#data={'emaila':}
		
		#db = pymongo.Connection('10.37.129.4',27017)
		#userdb=db.conn['DDSCDBA']
		#userdb.userlist.insert({'username':username,'password':encryptstr,
		#'company':companyname,'emaila':emaila,registerdate:datetime.now})
