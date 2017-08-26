def eval_loop(a):
  return eval(a)

x=raw_input("Enter the string to evaluate, Enter exit to exit \n")
while(x!="exit"):
  print str(eval_loop(x))
  x=x=raw_input("Enter the string to evaluate, Enter exit to exit \n")