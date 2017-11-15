import operator
f=open("words.txt")
words=[]
dict={}
for line in f:
  a=line.split(",")
  for i in a:
    b=i.split(".")
    for j in b:
      c=j.split()
      for k in c:
        if k in words:
            dict[k]+=1
        else:
          words.append(k)
          dict[k]=1
       
print words
print len(words)
t = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0,10):
  print t[i]