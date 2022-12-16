import turtle

t = turtle.Turtle()
t.penup()

#draw straight line
t.goto(-30,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("red")
t.right(90)
t.forward(200)
t.penup()
t.goto(-30,50) #centering in the screen

#draw curves
t.pendown()
t.right(-90)
t.circle(-100,180)
t.penup()

#draw J
t.goto(180,50)
t.pendown()
t.pensize(10)
t.pencolor("red")
 
t.forward(-20)
t.left(90)
t.forward(150)
t.circle(-50,180)
t.penup()

#draw straight line
t.goto(240,50) 
t.pendown()
t.pensize(10)
t.pencolor("red")
 
t.right(180)
t.forward(200)

