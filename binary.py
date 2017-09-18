import time
def bisect(x,item):
  n=len(x)
  l=0
  h=n-1
  while(l<=h):
    m=int((l+h)/2)
    if(x[m]==item):
      return m
    elif (x[m]<item):
      l=m+1
    else:
      h=m-1
  return -1
      
x=[1,2,3,4,5,6,7,8]
item=5
t1=time.time()
r=bisect(x,item)
t2=t1=time.time()
if(r==-1):
  print "Item not found"
else:
  print "Item found at position %d"%r
  
print "Time taken: ",t2-t1