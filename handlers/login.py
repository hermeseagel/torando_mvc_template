import tornado.web
import tornado.ioloop
import tornado.gen
import libs.dbops 
import config.dbsets as dbset
import json
class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('username')
		
class LoginHandler(BaseHandler):
	
	def get(self):
		self.render('login.html')
		
	def post(self):
		emaila=self.get_argument('email')
		password=self.get_argument('pass1')
		dbquery=libs.dbops
		serverip=dbset.serverip
		db=dbset.db
		collect=dbset.collect
		port=dbset.port
		condition={'emaila':emaila}
		getpasswd=dbquery.query(serverip,port,db,collect,condition,key)
		if password != getpasswd:
			self.redirect("/")
			
		else:
			return True
			
class logoutHandler(login_method):
	def 
		
