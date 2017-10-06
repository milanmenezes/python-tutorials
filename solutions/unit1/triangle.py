def is_triangle(a,b,c):
  if(a>b+c):
    return False
  if(b>a+c):
    return False
  if(c>a+b):
    return False
  return True

x=raw_input("Enter the sides of triangle seperated by space\n")
x=x.split()
if(is_triangle(int(x[0]),int(x[1]),int(x[2]))):
  print "Triangle can be formed\n"
  
else:
  print "Triangle cannot be formed\n"
