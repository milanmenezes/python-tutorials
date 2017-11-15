dict={"alphabet":0,"digits":0,"punctuation":0,"spaces":0}
t=[]
def fun(x):
  global dict
  x=x.split("\n")
  for i in x:
    k=i.split()
    dict["spaces"]+=len(k)
    for j in k:
      for l in j:
        t.append(l)
  for i in t:
    if i.isdigit():
      dict["digits"]+=1
    elif i.isalpha():
      dict["alphabet"]+=1
    else:
      dict["punctuation"]+=1

x='''Hello, how
are you? 123'''
fun(x)
print dict