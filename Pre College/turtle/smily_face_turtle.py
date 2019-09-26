# Draw a smily face using turtle :)

# Setup
import turtle
t = turtle.Pen()

# Circle

# Position
t.up()
t.right(90)
t.forward(50)
t.left(90)
t.down()

# Draw
t.circle(150)

# Left Eye

# Position
t.up()
t.left(90)
t.forward(225)
t.left(90)
t.forward(50)
t.left(90)
t.down()

# Draw
t.forward(50)

# Right Eye

# Position
t.up()
t.left(90)
t.forward(100)
t.left(90)
t.down()

# Draw
t.forward(50)

# Mouth

# Position
t.up()
t.backward(125)
t.left(90)
t.forward(130)
t.left(105)
t.down()

# Draw
t.circle(80, 150)

# Keep open :)
turtle.done()
