import tornado.web
import tornado.ioloop
import tornado.gen
import pymongo
class  MainHandler(tornado.web.RequestHandler):
	def get(self):
		#db = pymongo.Connection('10.37.129.4',27017)
		#userdb=db.conn
		print('render html')
		self.render('index.html')
			

		