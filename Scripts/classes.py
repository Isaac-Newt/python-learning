class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(self):
    print self.name
    print self.age
    
# # # # # # # # # # #
    
# Override practice
class Employee(object):
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00  
