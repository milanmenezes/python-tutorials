a=raw_input("Enter first string\n")
b=raw_input("Enter second string\n")
a=sorted(a.lower())
b=sorted(b.lower())
if a==b:
  print "It is an anagram"
else:
  print "It is not an anagram"