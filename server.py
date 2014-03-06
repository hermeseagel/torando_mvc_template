import tornado.httpserver
import tornado.ioloop
import tornado.options
import settings as setting
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
port = '8080'
if __name__ =='__main__':
#	print(type(setting.application))
	try:	
		print('listen port up')
		setting.application.listen(port)
		print('begin Http service')
		tornado.ioloop.IOLoop.instance().start()
	except HTTPError as httpresan:
		print(httpresan)


