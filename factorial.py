def fact(x):
  if(x==1):
    return 1
  return x*fact(x-1)

x=eval(raw_input("Enter a number\n"))
print "The factorial of "+str(x)+" is: "+str(fact(x))