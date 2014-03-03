import motor 
serverip='10.37.129.4'
port='27017'
db='ddsclogdb'
collection='srvconfig'
usename='ddsc'
passwd='ddscdba'
uri='mongodb://'+usename+':'+passwd+'@'+serverip+':'+port+'/'+db
uri="mongodb://ddsco:ddscdba@10.37.129.4:27017/ddsclogdb"
print(uri)
client=motor.MotorClient(uri).open_sync()
print(type(client))
dbc=client[db]
logtype={'test':'aaa','test2':'bbb'}
b=dbc.sysconfig.find()
print(b)



