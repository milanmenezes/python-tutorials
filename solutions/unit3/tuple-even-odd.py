x=raw_input("Enter the tuple\n")
x=x.split()
even=[]
odd=[]
x=[eval(i) for i in x]
for i in x:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print "Even: "+str(tuple(even))
print "Odd: "+str(tuple(odd))