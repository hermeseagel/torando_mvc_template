import handlers.maindex  as maindexa
import handlers.register	 as reg
#print('start urllist')
urls = [(r'/',maindexa.MainHandler),(r'/reg|/reg+w',reg.reghandler),(r'/useradd|/user+w',reg.reghandler)]
