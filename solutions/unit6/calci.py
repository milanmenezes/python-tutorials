
class calc():
#   def __init__(self):
#     self.x=0
#     self.y=0
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def add(self):
    return self.x+self.y
  def sub(self):
    return self.x-self.y
  def mul(self):
    return self.x*self.y
  def div(self):
    if self.y!=0: return self.x/self.y
    else: return "Divide by zero"
  
x = calc(10,2)
print x.add()
print x.sub()
print x.mul()
print x.div()