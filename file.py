f=open("intro.txt")
words=[]
for line in f:
  words.extend(line.split())
  
print words
print len(words)