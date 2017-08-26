def gcd(a,b,n):
  if(a%n==0 and b%n==0):
    return n
  return gcd(a,b,n-1)

x=raw_input("Enter 2 numbers\n")
x=x.split()
a=eval(x[0])
b=eval(x[1])
print "The GCD is: "+ str(gcd(a,b,min(a,b)))