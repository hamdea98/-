import turtle
tr=turtle.Turtle()

tr.speed("fastest")
bob = turtle.Pen() #the "P" in Pen must be capital.
for i in range(700):
    bob.forward(i)
    bob.left(80)
    bob.forward(50)
    bob.right(i)
    bob.back(50)
    bob.left(i)
