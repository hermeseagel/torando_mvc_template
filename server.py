import tornado.httpserver
import tornado.ioloop
import tornado.options
import settings as setting
import sys
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


