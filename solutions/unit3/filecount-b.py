import operator
f=open("intro.txt")
words=[]
dict={'the':0, 'of':0, 'for':0, 'is':0, 'as':0, 'an':0}
for line in f:
  a=line.split(",")
  for i in a:
    b=i.split(".")
    for j in b:
      c=j.split()
      for k in c:
        if k in dict:
          dict[k]+=1
       
t=tuple(dict.items())
t = sorted(t, key=operator.itemgetter(0))
for i in t:
  print i