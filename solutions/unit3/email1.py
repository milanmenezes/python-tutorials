import operator
f=open("mbox-short.txt")
l=[]
dict={}
for line in f:
	flag=0
	for k in line.split():
		if(flag):
			if k in dict:
				dict[k]+=1
			else:
				dict[k]=1
			break
		else:
			if ('From' in k):
				flag=1

print dict
t=tuple(dict.items())
t = sorted(t, key=operator.itemgetter(1),reverse=True)
print "The most popular email id is: "+t[0][0]

