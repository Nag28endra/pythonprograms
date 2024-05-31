import turtle

t = turtle.Turtle()
t.speed(10)

# Draw the body of the bird
t.color("orange")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the wing of the bird
t.color("orange")
t.begin_fill()
t.left(90)
t.forward(50)
t.right(135)
t.forward(35)
t.right(90)
t.forward(35)
t.right(135)
t.forward(50)
t.end_fill()

# Draw the other wing of the bird
t.color("orange")
t.begin_fill()
t.left(180)
t.forward(50)
t.right(135)
t.forward(35)
t.right(90)
t.forward(35)
t.right(135)
t.forward(50)
t.end_fill()

# Draw the head of the bird
t.color("yellow")
t.begin_fill()
t.left(135)
t.forward(35)
t.right(90)
t.forward(35)
t.right(135)
t.forward(50)
t.end_fill()

# Draw the eye of the bird
t.color("black")
t.begin_fill()
t.penup()
t.forward(20)
t.right(90)
t.forward(10)
t.pendown()
t.circle(3)
t.end_fill()

# Draw the beak of the bird
t.color("red")
t.begin_fill()
t.left(90)
t.forward(10)
t.right(135)
t.forward(7)
t.right(90)
t.forward(7)
t.right(135)
t.forward(10)
t.end_fill()

t.clone()
