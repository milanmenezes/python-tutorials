import operator
f=open("intro.txt")
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
          if k in dict:
            dict[k]+=1
        else:
          words.append(k)
          dict[k]=1
       
print words
print len(words)
sorted_x = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0,10):
  print sorted_x[i]