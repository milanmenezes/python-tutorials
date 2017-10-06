def sum(x):
  if(x==0):
    return 0
  return x+sum(x-1)

x=eval(raw_input("Enter a number\n"))
print "The sum to "+str(x)+ " natural numbers is: "+str(sum(x))