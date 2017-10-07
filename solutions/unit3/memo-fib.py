import time

def fib(n,memo):
  if n<2:
    return n
  if n not in memo:
    memo[n]=fib(n-2,memo)+fib(n-1,memo)
  return memo[n]

def fib1(n):
  if n<2: return n
  return fib1(n-2)+fib1(n-1)

def fibo(n):
  memo={0:0,1:1}
  return fib(n,memo)

x=eval(raw_input("Enter the number\n"))
t1=time.time()
print fibo(x)
t2=time.time()
print fib1(x)
t3=time.time()

print "Memo time: "+str(t2-t1)
print "Normal time: "+str(t3-t2)