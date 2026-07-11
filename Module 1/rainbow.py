import turtle

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# List of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the spiral
for i in range(200):
    pen.pencolor(colors[i % 7])  # Change color
    pen.forward(i * 2)           # Increase length
    pen.right(59)                # Turn angle

# Keep the window open
turtle.done()
