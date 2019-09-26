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
  
# # # # # # # # # #

class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2 
    self.angle3 = angle3
    
  number_of_sides = 3

  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
    else:
      return False
    
# Inherits from Triangle class
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# # # # # # # # # #

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
  def display_car(self):
    return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."

my_car = Car("DeLorean", "silver", 88)

print my_car.display_car()
