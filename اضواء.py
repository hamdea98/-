from turtle import*
import math

def k1():#Enemy Key Commands
    enemy.left(90)
    enemy.forward(10)
    enemy.right(90)

def k2():
    enemy.left(90)
    enemy.backward(10)
    enemy.right(90)

def k3():#Yertle Key Commands
    yertle.left(90)
    yertle.forward(10)
    yertle.right(90)

def k4():
    yertle.left(90)
    yertle.backward(10)
    yertle.right(90)

def k5():
    a=bullet_red()
    a.speed(10)
    a.forward(400)
    collision= math.sqrt(math.pow(a.xcor()-yertle.xcor(),2)+math.pow(a.ycor()-yertle.ycor(),2))
    if(collision<10):
        text=enemy.write("Game Over", align="center" , font=("Arial", 16, "normal"))
    a.hideturtle()

def k6():
    a=bullet_blue()
    a.speed(10)
    a.forward(400)
    collision= math.sqrt(math.pow(a.xcor()-yertle.xcor(),2)+math.pow(a.ycor()-yertle.ycor(),2))
    if(collision<10):
        text=enemy.write("Game Over", align="center" , font=("Arial", 16, "normal"))
    a.hideturtle()

def collision(a, b):
    collision= math.sqrt(math.pow(a.xcor()-b.xcor(),2)+math.pow(a.ycor()-b.ycor(),2))
    if(collision<5):
        print("Bottom Player Wins")
        print("Game Over")


def bullet_red():
    bullet=Turtle("circle")#Description For Bullet
    bullet.color("red")
    bullet.penup()
    bullet.goto(enemy.pos())
    bullet.setheading(180)
    bullet.right(90)
    return bullet

def bullet_blue():
    bullet=Turtle("circle")#Description For Bullet
    bullet.color("blue")
    bullet.penup()
    bullet.goto(yertle.pos())
    bullet.setheading(180)
    bullet.right(90)
    return bullet

ops = Screen()
ops.setup(500, 500)
ops.onkey(k1, "a")#Enemy
ops.onkey(k2, "d")#Enemy
ops.onkey(k3, "Left")#Yertle
ops.onkey(k4, "Right")#Yertle
ops.onkey(k5, "w")#Shoot(Enemy)
ops.onkey(k6, "Up")#Shoot(Enemy)
ops.listen()



checkpoint_1=Turtle(shape="circle")#Turtle Description for Checkpoint 1
checkpoint_1.color("red")
checkpoint_1.setheading(180)
checkpoint_1.right(90)
checkpoint_1.penup()
checkpoint_1.setx(-220)
checkpoint_1.sety(230)
checkpoint_1.speed(0)
#_____________________________

checkpoint_2=Turtle(shape="circle")#Turtle Description for Checkpoint 2
checkpoint_2.color("red")
checkpoint_2.setheading(180)
checkpoint_2.right(90)
checkpoint_2.penup()
checkpoint_2.setx(220)
checkpoint_2.sety(230)
checkpoint_2.speed(0)

#____________________________
runner=Turtle(shape="turtle")#Turtle Description for Checkpoint 2
runner.color("yellow")
while(runner!=collision):
    runner.penup()
    runner.goto(checkpoint_1.pos())
    runner.goto(checkpoint_2.pos())
    runner.speed(0)
    #_____________________________

enemy=Turtle(shape="turtle")#Turtle Description for Player 1
enemy.color("red")
enemy.setheading(180)
enemy.right(90)
enemy.penup()
enemy.setx(-20)
enemy.sety(-200)
enemy.speed(0)

    #_____________________________

yertle = Turtle(shape="turtle")#Turtle Description for Player 2
yertle.color("blue")
yertle.setheading(180)
yertle.right(90)
yertle.penup() 
yertle.setx(20)
yertle.sety(-200)
yertle.speed(0)
