result=[]

def enc(a,n,val):
  global result
  t=ord(a)
  t-=val
  t=(t+n)%26
  t+=val
  result.append(chr(t))
  
x=raw_input("Enter the string\n")
num=eval(raw_input("Enter the number\n"))

for i in x:
  if i.isupper():
    val=65
    enc(i,num,val)
  elif i.islower():
    val=97
    enc(i,num,val)
  else:
    result.append(i)
  
print "".join(result)