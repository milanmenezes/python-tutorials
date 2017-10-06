def trib(a,b,c,n):
  if n==0:
    return
  t=a+b+c
  print t,
  trib(b,c,t,n-1)
  
n=eval(raw_input("Enter n \n"))
print 0,1,1,
trib(0,1,1,n-3)