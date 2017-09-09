def enc(a,n,val):
  t=ord(a)
  t-=val
  t=(t+n)%26
  t+=val
  print chr(t),
  

x=raw_input("Enter the string\n")
num=eval(raw_input("Enter the number\n"))

for i in x:
  if x.isupper():
    val=65
  else:
    val=97
  enc(i,num,val)
  