l=[]
count=0
n=eval(raw_input())
for i in range(0,n):
  l.append(eval(raw_input()))
while(True):
  if(l==sorted(l)):
    break;
  for i in range(0,n-1):
    t=l[i]-l[i+1]
    if(t>=0):
      l[i]=t
  
  count+=1

print count