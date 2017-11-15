import time

memo={}
def fib(n):
  global memo
  if n<2:
    return n
  if n not in memo:
    memo[n]=fib(n-2)+fib(n-1)
  return memo[n]

def fib1(n):
  if n<2: return n
  return fib1(n-2)+fib1(n-1)

x=eval(raw_input("Enter the number\n"))
t1=time.time()
print fib(x)
t2=time.time()
print fib1(x)
t3=time.time()

print "Memo time: "+str(t2-t1)
print "Normal time: "+str(t3-t2)