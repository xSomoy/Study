file = 'test.txt'
fp = open(file, 'w')
fp.write('this is the first line')
fp.close()
#---------
file = 'test.txt'
fp = open(file,'a')
fp.write('\nthis is the second line')
fp.close()
#-----------
fp = open(file,'r')
print(fp.read())
#-----------
fp.seek(0)
print(fp.readlines())
fp.seek(1)
print(fp.readlines())
fp.close()
#-------------
with open(file, 'r') as fp:
	print(fp.read())
	
with open(file, 'r') as fp:
	data = fp.read()
print(data)