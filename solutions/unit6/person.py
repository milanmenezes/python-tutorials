import datetime
class person():
  def __init__(self,name,dob):
    self.name=name
    self.dob=dob
  
  #modifier function
  def update(self,dob):
    self.dob=dob
  
  #pure function
  def age(self):
    return datetime.datetime.now().year-self.dob.year

p1=person("Milan",datetime.datetime(1997,1,21))
print p1.age()
    