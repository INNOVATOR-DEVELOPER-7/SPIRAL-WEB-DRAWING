# import turtle
import turtle

sc = turtle.Screen()
sc.setup(400,400)

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(100)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(560):
	t.pencolor(colors[x%6]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
