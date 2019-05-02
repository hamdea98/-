import turtle
import random
import time
wn = turtle.Screen()
layout = turtle.Turtle()
layout.speed(100)
layout.up()

wn.bgcolor("lightgreen")
def drawTree(t, sd):
     for i in range(4):
         layout.down()
         t.forward(sd)
         t.right(90)
         layout.up()
 

def drawRiver():
    for i in range(2):
         print(layout.pos()[0])
         print(layout.pos()[1])
         layout.color("darkblue")
         layout.fillcolor("blue")
         layout.begin_fill()
         layout.down()
         layout.forward(2000)
         layout.right(90)
         layout.forward(99)
         layout.right(90)
         layout.forward(4000)
         layout.end_fill()
         layout.up()
   


def tree(branchLen,layout):
    if branchLen > 6:
         layout.down()
         layout.forward(branchLen)
         layout.right(20)
         tree(branchLen-6,layout)
         layout.left(40)
         tree(branchLen-6,layout)
         layout.right(20)
         layout.backward(branchLen)
         layout.up()

   
   

def main():
    myWin = turtle.Screen()
layout.left(90)
layout.up()
layout.backward(100)
layout.down()
layout.color("brown")
tree(36,layout)
layout.right(90)
layout.up()



def drawBridge():
    layout.goto(50, -120)
layout.down()
layout.color("rosybrown4")
layout.fillcolor("saddlebrown")
layout.begin_fill()
layout.forward(100)
layout.left(90)
layout.forward(150)
layout.left(90)
layout.forward(100)
layout.left(90)
layout.forward(150)
layout.left(90)
layout.up()
layout.end_fill()
layout.goto(150, -118)
layout.left(90)

layout.left(90)
for i in range(38):
    layout.pensize(.1)
    layout.down()
    layout.color("black")
    layout.forward(.1)
    layout.left(90)
    layout.forward(100)
    layout.left(90)
    layout.forward(.1)
    layout.left(90)
    layout.forward(100)
    layout.left(90)
    layout.up()
    layout.forward(4)
layout.up()
layout.right(90)

layout.goto(-799, 0)
drawRiver()
drawBridge()
# Tree locations
layout.goto(222, 198)
main()
layout.goto(-334, 155)
main()
layout.goto(132, 140)
main()
layout.goto(400, -200)
main()
layout.goto(50, -222)
main()
layout.goto(180, -122)
main()
layout.goto(-400, 400)
main()
layout.goto(-332, -332)
main()
layout.goto(-472, 400)
main()
layout.goto(-400, -380)
main()
layout.goto(-362,200)
main()
layout.goto(-222, 198)
main()
layout.goto(-750, -300)
main()
layout.goto(600, -467)
main()
layout.goto(100, 450)
main()
layout.goto(-100, 400)
main()
layout.goto(-600, 400)
main()
layout.goto(500, 123)
main()
layout.goto(700, 400)
main()
layout.goto(350, 350)
main()

layout.color("blue")
layout.goto(0, -50)
Player = turtle.Turtle()
Player.up()
Player.goto(0, -200)
Player.left(90)

def k1():
    Player.forward(45)

def k2():
    Player.left(30)

def k3():
    Player.right(30)

def k4():
    Player.back(45)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")

wn.listen()
