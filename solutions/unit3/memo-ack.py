memo={}
def ack(t1):
  global memo
  if(t1[0]==0):
    return t1[1]+1
  
  if(t1[0]>0 and t1[1]==0):
    tup1=(t1[0]-1,1)
    if tup1 not in memo:
      memo[tup1]=ack(tup1)
    return memo[tup1]
  
  if(t1[0]>0 and t1[1]>0):
    tup2=(t1[0],t1[1]-1)
    if tup2 not in memo:
      memo[tup2]=ack(tup2)
    tup3=(t1[0]-1,memo[tup2])
    if tup3 not in memo:
      memo[tup3]=ack(tup3)
    return memo[tup3]
  
x=tuple((eval(i) for i in raw_input("Enter 2 values\n").split()))
ack(x)