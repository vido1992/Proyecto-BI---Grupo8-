__author__ = 'diegoguaman'

'''


 QUITO
==============
'''
import couchdb
import sys
import urllib2
import re
import json

regex = re.compile(r'[A-z a-z 0-9]+')

from couchdb import view

URL = 'localhost'
db_name = 'belgica'


'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print (db_name)
    db = server[db_name]
    print ('success')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/belgica/_design/belgica28JuneCoordenadas/_view/belgica28JuneCoordenadas'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []
for x in d['rows']:
	a = x ['value']

	data ['people'].append({'text': x })
	with open ('CoordenadasBelgica.txt' , 'w') as outfile:
		json.dump(data,outfile)
		print (data)
f.close()
