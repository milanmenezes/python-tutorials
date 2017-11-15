import re
import operator
f=open("mbox-short.txt")
l=[]
dict={}
for line in f:
  l.extend(re.findall('From: [\w\.-]+@[\w\.-]+\.\w+', line))
  l.extend(re.findall('From [\w\.-]+@[\w\.-]+\.\w+', line))
  
for i in range(len(l)):
  l[i]=l[i].replace("From: ","")
  l[i]=l[i].replace("From ","")
  
for i in l:
  print i
  if(i in dict):
    dict[i]+=1
  else:
    dict[i]=1

t=tuple(dict.items())
t = sorted(t, key=operator.itemgetter(1),reverse=True)
print "The most popular email id is: "+t[0][0]
