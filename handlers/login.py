import tornado.web
import tornado.ioloop
import tornado.gen
import tornado.auth
import libs.dbops 
import query
import config.dbsets as dbset
import json
class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('username')
		
class LoginHandler(BaseHandler):
	 @tornado.web.authenticated
	def get(self):
		self.render('login.html')
		
	def post(self):
		emaila=self.get_argument('email')
		password=self.get_argument('pass1')
		condition={'emaila':emaila}
		getpasswd=query(condition)
		returnpwd=getpasswd.query_one()
		
		if password != returnpwd['password']:
			self.redirect("/")
			
		else:
			self.request.cookies()
			return True
			
class logoutHandler(login_method):
	def get(self)	:
		self.clear_cookie("authed_user")	

#class vailderpass:
#	def passcheck(,password):
#		query
		