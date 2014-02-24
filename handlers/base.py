import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options
#class BaseHandler(tornado.web.RequestHandler):
#	"""Base Class for common handler method """
#	 @tornado.web.asynchronous
class upload_form(tornado.web.RequestHandler):
	def uploadrender(self):
		self.reder('template/upload.html')
	def getpostfile(self):
		postfiled= self.request.files[''][0]
		fname=postfield['filename']
		output_file = open("uploads/"+fname,'wb')
		output_file.write()
		self.finish("file"+fname+"OK")
		
#	def 
