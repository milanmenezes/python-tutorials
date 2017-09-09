def square(x):
  return x**2

x=eval(raw_input("Enter the number\n"))
if(x>0 and x%2):
  print "The square of "+str(x)+" is: "+str(square(x))
  
else:
  print "Enter a valid number"