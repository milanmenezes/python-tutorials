f=open("intro.txt")
words=[]
for line in f:
  words.extend(line.split())
  
words = set(words)
print words
print len(words)