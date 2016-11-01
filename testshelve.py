rec1 = {'name': {'first': 'Bob', 'last': 'Smith'},
		'job': ['dev', 'mgr'],
		'age': 40.5}

rec2 = {'name': {'first': 'Sue', 'last': 'Jones'},
		'job': ['mgr'],
		'age': 35}

import shelve
db = shelve.open('dbfile')
db['bob'] = rec1
db['sue'] = rec2
db.close()

import shelve
db = shelve.open('dbfile')
for key in db:
	print(key, '=>', db[key])

bob = db['bob']
bob['age'] += 1
db['bob'] = bob
for key in db:
	print(key, '=>', db[key])
db.close()