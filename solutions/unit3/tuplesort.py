import operator
l1=[("Milan",20,10),("Mridul",19,9),("Mridul",17,9)]
l1=sorted(l1,key=operator.itemgetter(2))
l1=sorted(l1,key=operator.itemgetter(1))
l1=sorted(l1,key=operator.itemgetter(0))
for i in l1:
  print i