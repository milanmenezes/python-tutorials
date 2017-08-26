def pow(a,b):
  if(a==b):
    return True
  if((a%b)==0):
    return pow(a/b,b)
  return False

x=raw_input("Enter a and b\n")
x=x.split()
if(pow(eval(x[0]),eval(x[1]))):
  print x[0]+" is power of "+x[1]
  
else:
  print x[0]+" is not a power of "+x[1]