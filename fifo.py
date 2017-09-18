l=[]
while(True):
  x=eval(raw_input("Enter 1 to insert, 2 to delete 0 to quit\n"))
  if(x==1):
    y=eval(raw_input("Enter the element to be inserted\n"))
    l.append(y)
    
  elif(x==2):
    y=l.pop(0)
    print y
  
  elif(x==0):
    break