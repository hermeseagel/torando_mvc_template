import tornado.web
import tornado.ioloop
import tornado.gen
import tornado.auth
import datetime,os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
import  libs.logparser as logparser
__uploads__="loguploads/"
class  fileuploadhandler(tornado.web.RequestHandler):
	def get(self):
		print('render fileupload.html')
		self.render('upload.html')
class upload(tornado.web.RequestHandler):
	def post(self):
		fileinfo=self.request.files['filearg'][0]
		print(type(fileinfo))
		year=str(datetime.date.today())[0:4]
		month=str(datetime.date.today())[5:7]
		fname=fileinfo['filename']
		cusid='hermestest'
		cname=cusid+'_'+year+month+'_'+fname
		'''Cusid now just template test'''

		datestamp=year+month
		savelocation=open(__uploads__ + cname,'wb').write(fileinfo['body'])
		self.finish(cname + " is uploaded!! prepare logparser")
		logparser.dblogparser.parser(__uploads__,cname,datestamp)
		