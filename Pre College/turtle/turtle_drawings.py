import turtle

t = turtle.Pen()

# Draw a square
i = 0
while i < 4:
    t.forward(150)
    t.left(90)
    i += 1
    
t.reset()

# Draw an equilateral triangle
# Use thicker lines :)
t.width(5)
i = 0
while i < 3:
    t.backward(150)
    t.left(120)
    i += 1
    
t.reset()

# Draw a circle
t.width(2)
t.circle(150)
