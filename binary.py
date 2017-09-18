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
r=bisect(x,item)
if(r==-1):
  print "Item not found"
else:
  print "Item found at position %d"%r