def gcd(a,b):
  if(a==0):
    return b
  return gcd(b%a,a)

x=raw_input("Enter 2 numbers\n")
x=x.split()
a=eval(x[0])
b=eval(x[1])
print "The GCD is: "+ str(gcd(a,b))