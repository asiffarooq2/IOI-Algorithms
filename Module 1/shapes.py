import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Fun with Shapes")
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)
pen.width(3)

# Draw a square
pen.color("red")
for i in range(4):
    pen.forward(100)
    pen.right(90)

# Move to a new position
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw a triangle
pen.color("blue")
for i in range(3):
    pen.forward(100)
    pen.left(120)

# Move to another position
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a pentagon
pen.color("green")
for i in range(5):
    pen.forward(80)
    pen.left(72)

# Move to another position
pen.penup()
pen.goto(0, -150)
pen.pendown()

# Draw a hexagon
pen.color("purple")
for i in range(6):
    pen.forward(70)
    pen.left(60)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
