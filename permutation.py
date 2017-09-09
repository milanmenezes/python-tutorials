from itertools import permutations
a=raw_input("Enter the string\n")
a.split()
# for x in permutations(a):
#   print "".join(x)
print "\n".join(list("".join(x) for x in permutations(a)))


  
