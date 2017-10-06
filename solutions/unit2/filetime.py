import time
words=[]
words1=[]
def first():
  f=open("words.txt")
  global words
  for line in f:
    for i in line.split():
      words.append(i)
  
  
def second():
  f=open("words.txt")
  global words1
  for line in f:
    for i in line.split():
      words1+=i.split()
      
t1=time.time()
first()
print words
t2=time.time()
print "====================================================================="
t3=time.time()
second()
print words1
t4=time.time()
print "Time taken for append: ",t2-t1
print "Time taken for +: ",t4-t3