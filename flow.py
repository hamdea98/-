import turtle
ob=turtle.Turtle()
ob.speed(20)
d=200
angle=140
for i  in range(1,100):
    ob.forward(d)
    ob.left(angle)
    d=d-1
