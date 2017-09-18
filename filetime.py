import time
f=open("intro.txt")
words=[]
words1=[]
def first():
  global f
  global words
  for line in f:
    for i in line.split():
      words.append(i)
  
  
def second():
  global f
  global words1
  for line in f:
    for i in line.split():
      words1+=i
      
t1=time.time()
first()
t2=time.time()
print words
t3=time.time()
first()
t4=time.time()
print words
print "Time taken for append: ",t2-t1
print "Time taken for +: ",t4-t3