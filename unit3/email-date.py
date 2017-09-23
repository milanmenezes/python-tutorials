import re
import operator
f=open("mbox-short.txt")
l=[]

for line in f:
  l.extend(re.findall(r'From [\w\.-]+@[\w\.-]+\.\w+ \w+ \w+  \d+ \d+:\d+:\d+ \d+', line))
  
for i in range(len(l)):
  l[i]=l[i].split()
  
for i in l:
  print "Email received from: "+i[1]+" Date: "+i[2]+" "+i[3]+" "+i[4]+" "+i[6]+" Time: "+i[5]
