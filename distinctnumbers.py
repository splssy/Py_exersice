
# a: 1-9
# b: 0-9
# c: 0-9

l = range(10)
count = 0

for a in l[1:]:
    for b in l:
        if a == b: continue #filter1
	for c in l:
	    if c != a and c != b:
	       print(a,b,c)
	       count += 1

print('total distinct numbers within 100-999: %d'%count)
	
