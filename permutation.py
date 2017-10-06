from itertools import permutations
a=raw_input("Enter the string\n")

for x in permutations(a):
  print "".join(x)


  
