def is_sorted(x):
  if(x==sorted(x)):
    return True
  return False

x=[1,2,3,4,5]
if(is_sorted(x)):
  print "List is sorted"
  
else: print "List is not sorted"