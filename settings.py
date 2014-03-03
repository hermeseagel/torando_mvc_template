import tornado.web
import urls as urlmodule
import os
urls=urlmodule.urls
#print(urls)
#print('read setting')
SETTINGS=dict(template_path=os.path.join(os.path.dirname(__file__),"templates"),
static_path = os.path.join(os.path.dirname(__file__),"static"),libs_path = os.path.join(os.path.dirname(__file__),"libs")
,xfrf_cookies = True,debug = True)
print(SETTINGS)
try:
	print('call handler')
	
	application = tornado.web.Application(handlers = urls, **SETTINGS)
except (IOError,os.error) as resason:
	print(resason)