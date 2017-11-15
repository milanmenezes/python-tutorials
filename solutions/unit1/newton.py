from math import sqrt

def newton(a):
  x=a/2.0
  y=0
  while True:
    y=(x+a/x)/2.0
    if(x==y):
      return x
    x=y

print "num\t","math.sqrt(num)\t\t","Newton's method"
for i in range(1,11):
  print "%.1f"%i,"\t","%.10f"%sqrt(i),"\t\t","%.11f"%newton(i)
