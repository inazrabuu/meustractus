#with open("htmlget.txt", "r") as f:
#	fread = f.read().decode('utf-16').encode('ascii', 'ignore')
#	dataText = fread.splitlines(True)#

#for line in dataText:
#	print line.strip()

def changeme(mylist):
	mylist += " me"
	print "value inside function is ", mylist
	return

mylist = "test"
changeme(mylist)
print "value outside function is", mylist