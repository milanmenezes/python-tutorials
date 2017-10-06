def cum(x):
  sum=0
  y=[]
  for i in x:
    sum+=eval(i)
    y.append(str(sum)) 
  return y
             
x=raw_input("Enters the numbers seperated by space\n")
x=x.split()
y=cum(x)
print " ".join(y)