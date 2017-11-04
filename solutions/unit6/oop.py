class shape():
  def __init__(self,t):
    self.t=t
    self.area=0
    self.perim=0
  
  def __str__(self):
    return "Area: %d\nPerimeter: %d"%(self.area,self.perim)
  
class rect(shape):
  def __init__(self,l,b):
    self.l=l
    self.b=b
    self.area=l*b
    self.perim=2*(l+b)
    self.t="rect"
    
  def __add__(self,r):
    return rect(self.l+r.l,self.b+r.b)
    
class square(shape):
  def __init__(self,l):
    self.l=l
    self.area=l*l
    self.perim=4*l
    self.t="square"
    
  def __add__(self,r):
    return square(self.l+r.l)
  
sq1=square(4)
sq2=square(5)
sq3=sq1+sq2
print sq3
r1=rect(2,3)
r2=rect(4,5)
r3=r1+r2
print r3

    

 