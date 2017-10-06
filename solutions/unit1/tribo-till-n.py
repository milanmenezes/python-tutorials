def trib(a,b,c,n):
  if c>n:
    return
  print c,
  t=a+b+c
  trib(b,c,t,n)
  
n=eval(raw_input("Enter n>1 \n"))
print 0,1,
trib(0,1,1,n)